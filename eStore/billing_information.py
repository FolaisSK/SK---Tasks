from eStore.credit_card_information import CreditCardInformation


class BillingInformation:
    def __init__(self, receiver_name, receiver_phone_number, delivery_address, credit_card_information: CreditCardInformation):
        self.__receiver_name = receiver_name
        self.__receiver_phone_number = receiver_phone_number
        self.__delivery_address = delivery_address
        self.__credit_card_information = credit_card_information