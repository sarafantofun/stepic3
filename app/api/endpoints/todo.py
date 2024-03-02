from fastapi import APIRouter

from app.api.db.models.users import Todo

router = APIRouter(prefix="/todo", tags=["Todo"])


@router.post("/todo")
async def create_todo(data: Todo):
    Todo.create(data)
    return Todo
