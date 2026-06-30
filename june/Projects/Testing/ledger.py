class TransactionLedger:
    """A ledger to manage financial trasanctions, track balances, and categorize history"""

    def __init__(self, starting_balance: float = 0.0):
        self.balance = float(starting_balance)
        self.transactions = []

    def add_transaction(self, amount: float, category: str) -> float:
        """Adds a deposit (positive) or withdrawal (negative) to the ledger."""
        if self.balance + amount < 0:
            raise ValueError("Insufficient funds.")

        self.balance += amount
        transaction_record = {"amount": amount, "category": category}
        self.transactions.append(transaction_record)
        return self.balance
