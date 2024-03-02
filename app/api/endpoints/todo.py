from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db import get_db_session
from app.api.schemas import Todo as TodoCreate
from app.api.db.models.users import Todo as DBTodo
from app.api.endpoints.auth import get_current_user


router = APIRouter(prefix="/todo", tags=["Todo"])


@router.post("/todo")
async def create_todo(
    data: TodoCreate = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    db_todo = DBTodo(title=data.title, description=data.description)
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo
