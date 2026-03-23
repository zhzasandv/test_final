from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Genre
from schemas import GenreSchema

router = APIRouter(prefix="/api/v1/genres", tags=["genres"])


@router.get("/", response_model=list[GenreSchema])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()
