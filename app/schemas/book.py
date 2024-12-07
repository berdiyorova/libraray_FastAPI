from pydantic import BaseModel, Field


class BookIn(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    description: str
    isbn: str = Field(unique=True, max_length=20)
    author: int


class BookOut(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=255)
    description: str
    isbn: str = Field(unique=True, max_length=20)
    author: int