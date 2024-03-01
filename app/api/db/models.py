from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role: UserRole = mapped_column(default=UserRole.guest)


# class Token(Base):
#     access_token: Mapped[str]
#     token_type: Mapped[str]
#
#
# class TokenData(Base):
#     username: Mapped[str] | None = mapped_column(default=None)
