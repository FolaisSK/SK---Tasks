from eStore.product import Product


class Items:
    def __init__(self, quantity, product: Product):
        self.quantity = quantity
        self.product = product