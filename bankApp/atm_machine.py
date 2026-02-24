from bank import Bank


class AtmMachine:

    def __init__(self):
        self.bank = Bank("SK World Bank")

    def main(self):
        self.display_main_menu()

    def display_main_menu(self):
        main_menu = """
Welcome to Sk World Bank!!!
1 -> Create Account
2 -> Deposit
3 -> Withdraw
4 -> Transfer
5 -> Check Balance
6 -> Exit
"""
        response = input(main_menu).strip()
        match response:
            case '1':
                self.create_account()
            case '2':
                self.deposit()
            case '3':
                self.withdraw()
            case '4':
                self.transfer()
            case '5':
                self.check_balance()
            case '6':
                self.exit()
            case _:
                self.main()

    def create_account(self):
        name = input("Enter Name: ")
        phone_number = input("Enter Phone Number: ")
        pin = input("Enter 4 digit Pin: ")

        try:
            account = self.bank.create_account(name, pin, phone_number)
            print("Account created successfully")
            print("Your Account Number is:", account.get_account_number())
        except Exception as e:
            print(e)
        finally:
            self.display_main_menu()

    def deposit(self):
        account_number = input("Enter Account Number: ")

        try:
            amount = int(input("Enter Amount: "))
            self.bank.deposit(account_number, amount)
            print("Deposit successful")
        except Exception as e:
            print(e)
        finally:
            self.display_main_menu()

    def withdraw(self):
        account_number = input("Enter Account Number: ")
        pin = input("Enter Pin Number: ")

        try:
            amount = int(input("Enter Amount: "))
            self.bank.withdraw(account_number, amount, pin)
            balance = self.bank.check_balance(account_number, pin)
            print("Withdraw successful!!!")
            print("New Balance:", balance)
        except Exception as e:
            print(e)
        finally:
            self.display_main_menu()

    def transfer(self):
        sender_account = input("Enter Your Account Number: ")
        receiver_account = input("Enter Receiver Account Number: ")
        pin = input("Enter Pin Number: ")

        try:
            amount = int(input("Enter Amount: "))
            self.bank.transfer(sender_account, amount, pin, receiver_account)
            print("Transfer Successful!!")

            balance = self.bank.check_balance(sender_account, pin)
            print("Balance is:", balance)
        except Exception as e:
            print(e)
        finally:
            self.display_main_menu()

    def check_balance(self):
        account_number = input("Enter Your Account Number: ")
        pin = input("Enter Pin Number: ")

        try:
            balance = self.bank.check_balance(account_number, pin)
            print("Balance is:", balance)
        except Exception as e:
            print(e)
        finally:
            self.display_main_menu()

    def exit(self):
        print("Thank you for using Sk World Bank")
        quit()



if __name__ == "__main__":
    AtmMachine.main(self=AtmMachine())
