from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Author
from schemas import AuthorSchema

router = APIRouter(prefix="/api/v1/authors", tags=["authors"])


@router.get("/", response_model=list[AuthorSchema])
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()
