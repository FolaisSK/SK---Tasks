from bankApp.account import Account


class Bank:

    def __init__(self, name: str):
        self.__name = name
        self.__accounts = []

    def create_account(self, name: str, pin: str, phone_number: str) -> Account:
        account = Account(name, pin, phone_number)
        account.set_account_number()
        self.__accounts.append(account)
        return account

    def get_name(self) -> str:
        return self.__name

    def get_all_accounts(self) -> list:
        return self.__accounts

    def check_balance(self, account_number: str, pin: str) -> int:
        found_account = self.__get_account_by_account_number(account_number)
        self.__validate_account(found_account)
        return found_account.get_balance(pin)

    def deposit(self, account_number: str, amount: int):
        found_account = self.__get_account_by_account_number(account_number)
        self.__validate_account(found_account)
        found_account.deposit(amount)

    def withdraw(self, account_number: str, amount: int, pin: str):
        found_account = self.__get_account_by_account_number(account_number)
        self.__validate_account(found_account)
        found_account.withdraw(amount, pin)

    def transfer(self, sender_account_number: str, amount: int, pin: str, receiver_account_number: str):
        sender_account = self.__get_account_by_account_number(sender_account_number)
        self.__validate_account(sender_account)

        receiver_account = self.__get_account_by_account_number(receiver_account_number)
        self.__validate_account(receiver_account)

        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def __get_account_by_account_number(self, account_number: str):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def __validate_account(self, account):
        if account is None:
            raise ValueError("Account does not exist")
