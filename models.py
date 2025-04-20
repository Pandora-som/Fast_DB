from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Movie(Base):
    __tablename__="movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_name = Column(String(255))
    year = Column(Integer)
    genres = Column(String(400))
    time = Column(String(100))
    rate = Column(Float)
    description = Column(String)
    poster = Column(String)
    date_add = Column(String)

class Genre(Base):
    __tablename__="genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String(255))
    description = Column(String)
    
class Movie_Genre(Base):
    __tablename__="movie_genre"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))
