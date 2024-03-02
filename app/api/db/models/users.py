from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from enum import Enum as PyEnum
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.api.db.models.base import Base

if TYPE_CHECKING:
    from app.api.db.models import Todo


class UserRole(PyEnum):
    admin = "admin"
    user = "user"
    guest = "guest"


class User(Base):
    username: Mapped[str] = mapped_column(String(15), unique=True)
    password: Mapped[str]
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.guest)
    todos: Mapped[list["Todo"]] = relationship(back_populates="user")
