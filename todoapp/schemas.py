from typing import Optional

from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
