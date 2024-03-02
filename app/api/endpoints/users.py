from fastapi import APIRouter
from passlib.context import CryptContext


router = APIRouter(prefix="/users", tags=["Users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
