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

    genre1 = m.Genre(genre_name="Триллер", description="Фильм-катастрофа")
    session.add(genre1)
    genre2 = m.Genre(genre_name="Боевик", description="")
    session.add(genre2)

    movie_genre1 = m.Movie_Genre(movie_id="1", genre_id="1")
    session.add(movie_genre1)

    session.commit()
