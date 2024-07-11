from pydantic import BaseModel
from pydantic import ConfigDict


class CategoryBase(BaseModel):
    name: str


class CategoryRead(CategoryBase):
    id: int


class FilmBase(BaseModel):
    title: str
    description: str
    year: int
    rating: float
    file_path: str
    picture_path: str


class FilmRead(FilmBase):
    id: int
