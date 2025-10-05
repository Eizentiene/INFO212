from app.transaction import Transaction

transactions = []

def add_transaction():
    description = input("Enter transaction description: ")
    while True:
        try:
            amount = float(input("Enter transaction amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    t = Transaction(description, amount)
    transactions.append(t)
    print(f"Transaction added: {t}")

def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    print("\nAll transactions:")
    for t in transactions:
        print(f"- {t}")

def main():
    print("Welcome to Finance Tracker MVP!")
    while True:
        print("\nOptions:\n1. Add transaction\n2. View transactions\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
