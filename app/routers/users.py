from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.core.database import SessionDep
from app.core.models.user import UserModel
from app.schemas import UserIn, UserOut

router = APIRouter(
    tags=["users"]
)

@router.post("/users/", response_model=UserOut, status_code=201)
async def create_user(user: UserIn, session: SessionDep):
    try:
        user_in = UserModel(**user.dict())
        session.add(user_in)
        session.commit()
        session.refresh(user_in)
        return user_in
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong")


@router.get("/users/", status_code=200)
async def get_users(session: SessionDep) -> list[UserOut]:
    users = session.exec(select(UserModel)).all()
    return users


@router.get("/users/{user_id}", response_model=UserOut, status_code=200)
async def get_user(session: SessionDep, user_id: int):
    user = session.exec(select(UserModel).where(UserModel.id == user_id)).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.delete("/users/{user_id}/", status_code=200)
async def delete_user(user_id: int, session: SessionDep) -> dict:
    user = session.get(UserModel, user_id)
    # user = session.exec(select(UserModel).where(UserModel.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"status": True, "detail": "User is deleted"}


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
