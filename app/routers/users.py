from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select

from app.core.database import SessionDep
from app.core.models.user import UserModel
from app.core.security.jwt_token import get_current_active_user
from app.core.security.permissions import is_admin, is_user, is_admin_or_user
from app.schemas.user import UserIn, UserOut

router = APIRouter(
    tags=["users"]
)



@router.get("/users/", status_code=200)
async def get_users(session: SessionDep) -> list[UserOut]:
    users = session.exec(select(UserModel)).all()
    return users


@router.get("/users/me/", response_model=UserModel)
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/admin/", response_model=UserModel, dependencies=[Depends(is_admin)])
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/user/", response_model=UserModel, dependencies=[Depends(is_user)])
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/admin/user/", response_model=UserModel, dependencies=[Depends(is_admin_or_user)])
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_active_user)],
):
    return current_user



@router.put("/users/{user_id}/", status_code=200)
async def update_user(user_id: int, user_in: UserIn, session: SessionDep) -> dict:
    user = session.exec(select(UserModel).where(UserModel.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = user_in.username
    user.first_name = user_in.first_name
    user.last_name = user_in.last_name
    user.age = user_in.age

    session.commit()
    return user
