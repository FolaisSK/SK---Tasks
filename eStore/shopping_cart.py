from eStore.items import Items

from typing import List


class ShoppingCart:
    def __init__(self):
        self.items: list[Items] = []