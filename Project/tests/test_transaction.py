from app.transaction import Transaction

def test_transaction_creation():
    t = Transaction("Lunch", -12.5)
    assert t.description == "Lunch"
    assert t.amount == -12.5
