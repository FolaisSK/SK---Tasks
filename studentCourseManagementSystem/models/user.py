from pydantic import BaseModel

from models.enums import UserRole


class User(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole

