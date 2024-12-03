from sqlmodel import SQLModel, Field

from app.core.database import engine


class BookModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(min_length=3, max_length=255)
    description: str
    isbn: str = Field(unique=True, max_length=20)
    author: int = Field(foreign_key="usermodel.id", ondelete="CASCADE")


async def create_book_table():
    SQLModel.metadata.create_all(bind=engine)
