from app.transaction import Transaction

def test_transaction_list():
    transactions = []
    t = Transaction("Test", 10)
    transactions.append(t)
    assert len(transactions) == 1
    assert transactions[0].description == "Test"
    assert transactions[0].amount == 10