import unittest
from bankApp.bank import Bank


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("SK Bank")

    def test_that_account_can_be_created(self):
        account = self.bank.create_account("Fola", "1234", "08012345678")

        self.assertIsNotNone(account)
        self.assertEqual("SK Bank", self.bank.get_name())
        self.assertEqual(1, len(self.bank.get_all_accounts()))

    def test_to_deposit_5k_balance_is_5k(self):
        account = self.bank.create_account("Fola", "1234", "08012345678")
        account_number = account.get_account_number()

        self.bank.deposit(account_number, 5000)

        self.assertEqual(5000, self.bank.check_balance(account_number, "1234"))

    def test_to_deposit_5k_withdraw_2k_balance_is_3k(self):
        account = self.bank.create_account("Fola", "1234", "08012345678")
        account_number = account.get_account_number()

        self.bank.deposit(account_number, 5000)
        self.bank.withdraw(account_number, 2000, "1234")

        self.assertEqual(3000, self.bank.check_balance(account_number, "1234"))

    def test_that_withdraw_with_wrong_pin_throws_exception(self):
        account = self.bank.create_account("Fola", "1234", "08012345678")
        account_number = account.get_account_number()

        self.bank.deposit(account_number, 5000)

        with self.assertRaises(ValueError):
            self.bank.withdraw(account_number, 2000, "0000")

    def test_that_transfer_works_correctly(self):
        sender = self.bank.create_account("Fola", "1234", "08012345678")
        receiver = self.bank.create_account("Tobi", "5678", "08087654321")

        sender_account_number = sender.get_account_number()
        receiver_account_number = receiver.get_account_number()

        self.bank.deposit(sender_account_number, 10000)

        self.bank.transfer(sender_account_number, 4000, "1234", receiver_account_number)

        self.assertEqual(6000, self.bank.check_balance(sender_account_number, "1234"))
        self.assertEqual(4000, self.bank.check_balance(receiver_account_number, "5678"))

    def test_that_transfer_throws_exception_with_wrong_pin(self):
        sender = self.bank.create_account("Fola", "1234", "08012345678")
        receiver = self.bank.create_account("Tobi", "5678", "08087654321")

        sender_account_number = sender.get_account_number()
        receiver_account_number = receiver.get_account_number()

        self.bank.deposit(sender_account_number, 10000)

        with self.assertRaises(ValueError):
            self.bank.transfer(sender_account_number, 4000, "0000", receiver_account_number)

    def test_that_check_balance_throws_exception_if_account_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.bank.check_balance("99999", "1234")

    def test_that_deposit_throws_exception_if_account_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.bank.deposit("99999", 5000)


if __name__ == "__main__":
    unittest.main()
