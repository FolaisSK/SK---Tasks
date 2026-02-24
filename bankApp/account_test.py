import unittest

from bankApp.account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("Fola", "1234", "09079368997")
        self.account_two = Account("Dave", "1111", "08145678912")

    def test_deposit5k_balance_is_5k(self):
        self.assertEqual(0, self.account.get_balance("1234"))

        self.account.deposit(5_000)
        self.assertEqual(5_000, self.account.get_balance("1234"))

    def test_balance_is_5k_deposit5k_balance_is_10k(self):
        self.assertEqual(0, self.account.get_balance("1234"))

        self.account.deposit(5_000)
        self.assertEqual(5_000, self.account.get_balance("1234"))

        self.account.deposit(5_000)
        self.assertEqual(10_000, self.account.get_balance("1234"))

    def test_balance_is_5k_deposit_minus_2k_balance_is_still_5k(self):
        self.assertEqual(0, self.account.get_balance("1234"))

        self.account.deposit(5_000)
        self.assertEqual(5_000, self.account.get_balance("1234"))

        with self.assertRaises(ValueError):
            self.account.deposit(-2_000)

        self.assertEqual(5_000, self.account.get_balance("1234"))

    def test_deposit5k_withdraw2k_balance_is_3k(self):
        self.account.deposit(5_000)
        self.account.withdraw(2_000, "1234")

        self.assertEqual(3_000, self.account.get_balance("1234"))

    def test_deposit2k_withdraw20k_balance_is_still_2k(self):
        self.account.deposit(2_000)

        with self.assertRaises(ValueError):
            self.account.withdraw(20_000, "1234")

        self.assertEqual(2_000, self.account.get_balance("1234"))

    def test_deposit5k_withdraw_minus2k_balance_is_still_5k(self):
        self.account.deposit(5_000)

        with self.assertRaises(ValueError):
            self.account.withdraw(-2_000, "1234")

        self.assertEqual(5_000, self.account.get_balance("1234"))

    def test_deposit10k_withdraw10k_balance_is_zero(self):
        self.account.deposit(10_000)
        self.account.withdraw(10_000, "1234")

        self.assertEqual(0, self.account.get_balance("1234"))

    def test_balance_is_zero_deposit10k_withdraw5k_balance_is_5k(self):
        self.account.deposit(10_000)
        self.account.withdraw(5_000, "1234")

        self.assertEqual(5_000, self.account.get_balance("1234"))

    def test_deposit10k_input_pin_balance_is_10k(self):
        self.account.deposit(10_000)
        self.assertEqual(10_000, self.account.get_balance("1234"))

    def test_deposit10k_input_wrong_pin_balance_is_zero(self):
        self.account.deposit(10_000)
        self.assertEqual(0, self.account.get_balance("1111"))

    def test_deposit10k_input_pin_withdraw5k_balance_is_5k(self):
        self.account.deposit(10_000)
        self.account.withdraw(5_000, "1234")

        self.assertEqual(5_000, self.account.get_balance("1234"))

    def test_deposit10k_input_wrong_pin_withdraw5k_balance_is_still_10k(self):
        self.account.deposit(10_000)

        with self.assertRaises(ValueError):
            self.account.withdraw(5_000, "1111")

        self.assertEqual(10_000, self.account.get_balance("1234"))


if __name__ == '__main__':
    unittest.main()
