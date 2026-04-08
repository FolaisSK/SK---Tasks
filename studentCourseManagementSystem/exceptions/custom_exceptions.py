from fastapi import HTTPException, status


class InvalidRoleException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid role not allowed"
        )

class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facilitator not found"
        )


class CourseNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )


class EmailAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

class EnrollmentNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enrollment not found"
        )

class EnrollmentAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Enrollment already exists"
        )

class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

class CourseAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course already exists"
        )

class InvalidGradeException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Grade"
        )