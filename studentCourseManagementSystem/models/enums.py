from enum import Enum


class UserRole(str, Enum):
    STUDENT = "student"
    FACILITATOR = "facilitator"

class Grades(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"