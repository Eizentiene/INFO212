class Transaction:
    def __init__(self, description, amount, category, timestamp):
        self.description = description
        self.amount = amount
        self.category = category
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.description} | {self.amount} NOK | {self.category} | {self.timestamp}"