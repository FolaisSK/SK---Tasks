from eStore.user import User


class Seller(User):
    def __init__(self, name, age, password, email_address, home_address, phone_number):
        super().__init__(name, age, password, email_address, home_address, phone_number)