from enum import Enum


class Category(str,Enum):
    FOOD = 'food'
    TRANSPORTATION = 'transportation'
    RENT = 'rent'
    ENTERTAINMENT = 'entertainment'
    SAVINGS = 'savings'
    OTHER = 'other'