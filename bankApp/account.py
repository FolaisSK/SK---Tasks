class Account:

    def __init__(self, name: str, pin: str, phone_number: str):
        self.__validate_name(name)
        self.__name = name
        self.__pin = pin
        self.__phone_number = phone_number
        self.__balance = 0
        self.__number = None

    def get_balance(self, pin_number: str) -> int:
        if pin_number == self.__pin:
            return self.__balance
        return 0

    def deposit(self, amount: int):
        self.__validate_positive_amount(amount)
        self.__balance += amount

    def withdraw(self, amount: int, pin_number: str):
        self.__validate_pin(pin_number)
        self.__validate_amount(amount)
        self.__validate_positive_amount(amount)
        self.__balance -= amount

    def set_account_number(self):
        self.__number = self.__generate_account_number()

    def get_account_number(self) -> str:
        return self.__number

    def __generate_account_number(self) -> str:
        self.__validate_phone_number()
        return self.__phone_number[1:]

    def __validate_phone_number(self):
        if len(self.__phone_number) != 11:
            raise ValueError("Invalid Phone Number")

    def __validate_pin(self, pin_number: str):
        if pin_number != self.__pin:
            raise ValueError("Invalid Pin")

    def __validate_amount(self, amount: int):
        if amount > self.__balance:
            raise ValueError("Insufficient Funds")

    def __validate_positive_amount(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid Amount")

    def __validate_name(self, name: str):
        if not name.strip():
            raise ValueError("What kind of name is that")
