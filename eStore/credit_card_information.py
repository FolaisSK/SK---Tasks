from eStore.card_tye import CardType


class CreditCardInformation:
    def __init__(self, cvv, expiration_year, expiration_month, card_number, name_on_card, card_type: CardType):
        self.cvv = cvv
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.card_number = card_number
        self.name_on_card = name_on_card
        self.card_type = card_type