from typing import List

from models import Todo
from schemas import TodoCreate

todos: List[Todo] = []

async def get_todos():
    return todos

async def create(todo: TodoCreate):
    new_id = len(todos)+1
    new_todo = await Todo(todo_id = new_id,
                    title=todo.title,
                    description=todo.description
                    )
    todos.append(new_todo)
    return new_todo