from sqlmodel import SQLModel, Field

from app.core.database import engine


class UserModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(min_length=3, max_length=100)
    first_name: str | None = Field(default=None, max_length=50)
    last_name: str | None = Field(default=None, max_length=50)
    age: int | None = Field(default=None, gt=0)


async def create_user_table():
    SQLModel.metadata.create_all(bind=engine)
