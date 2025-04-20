from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    movie1 = m.Movie(movie_name="Знамение",year="2009",genres="Триллер",
                     time="106 мин",rate="6",description="Фильм-катастрофа",
                     poster="/Ссылка на изображение",date_add="12.03.2012")
    session.add(movie1)
    
    genre1 = m.Genre(genre_name="Триллер",description="Фильм-катастрофа")
    session.add(genre1)

    session.commit()