from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.core.database import SessionDep
from app.core.models.book import BookModel
from app.schemas import BookOut, BookIn

router = APIRouter(
    tags=["books"]
)

@router.post("/books/", response_model=BookOut, status_code=201)
async def add_book(book_in: BookIn, session: SessionDep):
    try:
        book = BookModel(**book_in.dict())
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong")


@router.get("/books/", status_code=200)
async def get_books(session: SessionDep) -> list[BookOut]:
    books = session.exec(select(BookModel)).all()
    return books


@router.get("/books/{book_id}", response_model=BookOut, status_code=200)
async def get_user(session: SessionDep, book_id: int):
    book = session.exec(select(BookModel).where(BookModel.id == book_id)).one_or_none()
    if book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return book


@router.delete("/books/{book_id}/", status_code=200)
async def delete_book(book_id: int, session: SessionDep) -> dict:
    book = session.get(BookModel, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"status": True, "detail": "Book is deleted"}


@router.put("/books/{book_id}/", status_code=200)
async def update_book(book_id: int, book_in: BookIn, session: SessionDep) -> dict:
    book = session.exec(select(BookModel).where(BookModel.id == book_id)).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = book_in.title
    book.description = book_in.description
    book.isbn = book_in.isbn
    book.author = book_in.author

    session.commit()
    return book
