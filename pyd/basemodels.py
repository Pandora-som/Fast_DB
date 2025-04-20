from pydantic import BaseModel, Field
import datetime

class BaseMovie(BaseModel):
    id:int=Field(example=1)
    movie_name:str=Field(example="Знамение")
    year:int=Field(example="2009")
    genres:str=Field(example="Триллер")
    time:str=Field(example="106 мин")
    rate:float=Field(example="6")
    description:str=Field(example="Фильм-катастрофа")
    poster:str=Field(example="Ссылка на изображение")
    date_add:datetime.time=Field(example="12.03.2012")
    
class BaseGenre(BaseModel):
    id:int=Field(example=1)
    genre_name:str=Field(example="Триллер")
    description:str=Field(example="Фильм-катастрофа")
    
class BaseMovie_Genre(BaseModel):
    id:int=Field(example=1)
    movie_id:int=Field()
    genre_id:int=Field()
    
    
    