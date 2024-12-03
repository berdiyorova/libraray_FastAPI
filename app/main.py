from fastapi import FastAPI

from app.core.models.user import create_user_table
from app.core.models.book import create_book_table

from .routers import users, books


app = FastAPI()


@app.on_event("startup")
async def startup():
    await create_user_table()
    await create_book_table()

@app.get("/")
async def root():
    return "Welcome!"

app.include_router(users.router)
app.include_router(books.router)
