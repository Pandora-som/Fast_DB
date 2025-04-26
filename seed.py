from sqlalchemy.orm import Session
from database import engine
import models as m
from datetime import datetime as dt

m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    movie1 = m.Movie(
        movie_name="Знамение",
        year="2009",
        time="106",
        rate="6",
        description="Фильм-катастрофа",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie1)
    
    movie2 = m.Movie(
        movie_name="Пятый элемент",
        year="1997",
        time="126",
        rate="8.2",
        description="Спасение планеты",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie2)
    
    movie3 = m.Movie(
        movie_name="Васаби",
        year="2001",
        time="94",
        rate="7.6",
        description="Комедийный боевик о детективе",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie3)

    genre1 = m.Genre(genre_name="Триллер", description="")
    session.add(genre1)
    genre2 = m.Genre(genre_name="Боевик", description="")
    session.add(genre2)
    genre3 = m.Genre(genre_name="Комедия", description="")
    session.add(genre3)

    movie_genre1 = m.Movie_Genre(movie_id="1", genre_id="1")
    session.add(movie_genre1)
    movie_genre2 = m.Movie_Genre(movie_id="2", genre_id="1")
    session.add(movie_genre2)
    movie_genre3 = m.Movie_Genre(movie_id="2", genre_id="3")
    session.add(movie_genre3)
    movie_genre4 = m.Movie_Genre(movie_id="3", genre_id="2")
    session.add(movie_genre4)
    movie_genre5 = m.Movie_Genre(movie_id="3", genre_id="3")
    session.add(movie_genre5)

    session.commit()
