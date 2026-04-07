from pydantic import BaseModel


class Todo(BaseModel):
    todo_id: int
    title: str
    description: str
    completed: bool = False
