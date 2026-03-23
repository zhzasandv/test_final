from pydantic import BaseModel, computed_field
from typing import Optional

BASE_URL = "http://localhost:8000"


class AuthorSchema(BaseModel):
    id: int
    first_name: str
    last_name: str

    model_config = {"from_attributes": True}


class GenreSchema(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class BookSchema(BaseModel):
    id: int
    name: str
    price: float
    title: str
    publication_date: str
    genre: GenreSchema
    authors: list[AuthorSchema]
    oblojka: Optional[str] = None

    @computed_field
    @property
    def image_url(self) -> Optional[str]:
        if self.oblojka:
            return f"{BASE_URL}/media/{self.oblojka}"
        return None

    model_config = {"from_attributes": True}
