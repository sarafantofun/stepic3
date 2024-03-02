from sqlalchemy import Enum, String, Text, ForeignKey
from enum import Enum as PyEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class UserRole(PyEnum):
    admin = "admin"
    user = "user"
    guest = "guest"


class User(Base):
    username: Mapped[str] = mapped_column(String(15), unique=True)
    password: Mapped[str]
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.guest)


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


# class Token(Base):
#     access_token: Mapped[str]
#     token_type: Mapped[str]
#
#
# class TokenData(Base):
#     username: Mapped[str] | None = mapped_column(default=None)
