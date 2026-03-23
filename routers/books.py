from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import Book
from schemas import BookSchema

router = APIRouter(prefix="/api/v1/books", tags=["books"])


@router.get("/", response_model=list[BookSchema])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).options(
        joinedload(Book.authors),
        joinedload(Book.genre)
    ).all()
    return books
