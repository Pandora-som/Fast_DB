from pydantic import BaseModel, Field
from datetime import datetime, date


class CreateMovie(BaseModel):
    movie_name: str = Field(example="Знамение")
    year: int = Field(ge=1900, le=3000, example="2009")
    time: int = Field(gt=0, example="106")
    rate: float = Field(ge=0, le=10, example="6")
    description: str | None = Field(example="Фильм-катастрофа")
    poster: str = Field(example="Ссылка на изображение")
    date_add: date = Field(example="2012-12-12")


class CreateGenre(BaseModel):
    genre_name: str = Field(example="Триллер")
    description: str | None = Field(example="Фильм-катастрофа")


class CreateMovie_Genre(BaseModel):
    movie_id: int = Field()
    genre_id: int = Field()
