from pydantic import BaseModel, EmailStr

from models.enums import UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: UserRole