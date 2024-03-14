from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.future import select
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


@router.get("/{todo_id}")
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(DBTodo).filter(DBTodo.id == todo_id))
    todo_obj = result.scalars().first()
    if todo_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo_obj


@router.put("/{todo_id}")
async def update_todo(
    todo_id: int,
    data: TodoCreate,
    db: AsyncSession = Depends(get_db_session),
):
    result = await db.execute(select(DBTodo).filter(DBTodo.id == todo_id))
    todo_obj_update = result.scalars().first()
    if todo_obj_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todo_obj_update.title = data.title
    todo_obj_update.description = data.description
    await db.commit()
    return todo_obj_update
