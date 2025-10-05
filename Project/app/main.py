from datetime import datetime
import csv
from app.transaction import Transaction

transactions = []

# --- File handling ---
def save_transactions():
    with open("transactions.txt", "w") as f:
        for t in transactions:
            f.write(f"{t.description},{t.amount},{t.category},{t.timestamp}\n")

def load_transactions():
    try:
        with open("transactions.txt") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    desc, amt, cat, ts = parts
                    transactions.append(Transaction(desc, float(amt), cat, ts))
    except FileNotFoundError:
        pass

def export_to_csv():
    with open("transactions.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Description", "Amount", "Category", "Timestamp"])
        for t in transactions:
            writer.writerow([t.description, t.amount, t.category, t.timestamp])
    print("Transactions exported to transactions.csv")

# --- AI/Mock categorization ---
def categorize_transaction(description):
    keywords = {
        "Food": ["lunch", "dinner", "restaurant", "cafe", "mcdonald", "kebab"],
        "Transport": ["bus", "train", "taxi", "uber", "fuel", "gas"],
        "Shopping": ["store", "supermarket", "amazon", "shopping"],
        "Entertainment": ["cinema", "movie", "game", "concert"]
    }
    desc_lower = description.lower()
    for category, words in keywords.items():
        if any(word in desc_lower for word in words):
            return category
    return "Other"

# --- Transaction functions ---
def add_transaction():
    description = input("Enter transaction description: ")

    while True:
        try:
            amount = float(input("Enter transaction amount: ").replace(',', '.'))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category (or leave blank for AI suggestion): ")
    if not category:
        category = categorize_transaction(description)
        print(f"AI-suggested category: {category}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    t = Transaction(description, amount, category, timestamp)
    transactions.append(t)
    save_transactions()
    print(f"Transaction added: {t}")

def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    print("\nAll transactions:")
    for t in transactions:
        color = "\033[92m" if t.amount >= 0 else "\033[91m"
        reset = "\033[0m"
        print(f"- {t.timestamp} | {t.description} | {t.category} | {color}{t.amount}{reset}")

def view_balance():
    total = sum(t.amount for t in transactions)
    print(f"\nTotal balance: {total}")

# --- Main program ---
def main():
    load_transactions()  # load at start
    print("Welcome to Finance Tracker MVP!")

    while True:
        print("\nOptions:")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. View balance")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            export_to_csv()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
