import os
import sys

# Look directly inside the current Testing folder for ledger.py
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest

from ledger import TransactionLedger  # This will now find it perfectly!


class TestTransactionLedger(unittest.TestCase):
    def setUp(self):
        """Runs before every test. Replaces the pytest fixture."""
        self.ledger = TransactionLedger(starting_balance=100.0)

    def test_initial_balance(self):
        # We can create a one-off instance to test default parameters
        standalone_ledger = TransactionLedger()
        self.assertEqual(standalone_ledger.balance, 0.0)

    def test_deposit(self):
        new_balance = self.ledger.add_transaction(50.0, "Salary")
        self.assertEqual(new_balance, 150.0)
        self.assertEqual(self.ledger.balance, 150.0)

    def test_insufficient_funds_raises_error(self):
        # Testing exceptions using a context manager in unittest
        with self.assertRaises(ValueError):
            self.ledger.add_transaction(-200.0, "Vacation")


if __name__ == "__main__":
    unittest.main()
