from fastapi import Depends

from app.api.schemas import User


@app.get("/protected_resource", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
