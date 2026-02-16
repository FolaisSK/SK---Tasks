from typing import List

from eStore.billing_information import BillingInformation
from eStore.shopping_cart import ShoppingCart
from eStore.user import User


class Customer(User):
    def __init__(self, name, age, password, email_address, home_address, phone_number):
        super().__init__(name, age, password, email_address, home_address, phone_number)
        self.billing_information: List[BillingInformation] = []
        self.shopping_cart = ShoppingCart()