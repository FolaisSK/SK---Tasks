class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'User Already Exists'
        super().__init__(self.message)

class InvalidEmailOrPasswordException(Exception):
    def __init__(self):
        self.message = "Invalid Email or Password"
        super().__init__(self.message)

class InvalidExpenseCategoryException(Exception):
    def __init__(self):
        self.message = "Invalid Expense Category"
        super().__init__(self.message)

class InvalidAmountException(Exception):
    def __init__(self):
        self.message = "Invalid Amount"
        super().__init__(self.message)

class ExpenseDoesNotExistException(Exception):
    def __init__(self):
        self.message = "Expense Does Not Exist"
        super().__init__(self.message)