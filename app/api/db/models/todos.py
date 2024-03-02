from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.api.db.models import Base

if TYPE_CHECKING:
    from app.api.db.models import User


class Todo(Base):
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    completed: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(back_populates="todos")
