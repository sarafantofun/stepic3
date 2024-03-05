from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db import get_db_session
from app.api.schemas import Todo as TodoCreate, User
from app.api.db.models.todos import Todo as DBTodo
from app.api.endpoints.auth import get_current_user


router = APIRouter(prefix="/todo", tags=["Todo"])


@router.post("")
async def create_todo(
    data: TodoCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    db_todo = DBTodo(
        title=data.title, description=data.description, user_id=current_user.id
    )
    db.add(db_todo)
    await db.commit()
    return {
        "message": f"Task {db_todo.title} successfully created",
    }
