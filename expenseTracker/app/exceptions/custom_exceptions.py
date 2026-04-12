from werkzeug.exceptions import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self, message):
        super().__init__(description=message,)
