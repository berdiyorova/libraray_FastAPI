from pydantic import BaseModel, Field

class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    first_name: str = Field(min_length=3, max_length=100)
    last_name: str | None = Field(default=None, min_length=3, max_length=100)
    age: int = Field(gt=0)


class UserOut(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=100)
    first_name: str = Field(min_length=3, max_length=100)
    last_name: str | None = Field(default=None, min_length=3, max_length=100)
    age: int = Field(gt=0)


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
