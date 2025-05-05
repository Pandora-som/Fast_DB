from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd
import shutil
from fastapi.staticfiles import StaticFiles
import string
import random
import os
from auth import basic_auth

app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")


@app.get("/movies", response_model=List[pyd.SchemeMovie])
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies


@app.get("/movies/{id}", response_model=pyd.SchemeMovie)
def get_movie(id: int, db: Session = Depends(get_db)):
    movie = db.query(m.Movie).filter(m.Movie.id == id).first()
    if not movie:
        raise HTTPException(404, "Фильм   не найден")
    return movie


@app.post("/movies", response_model=pyd.SchemeMovie)
def create_movie(
    movie: pyd.CreateMovie,
    db: Session = Depends(get_db),
    user: m.User = Depends(basic_auth),
):
    movie_db = m.Movie()
    movie_db.movie_name = movie.movie_name
    movie_db.year = movie.year
    movie_db.time = movie.time
    movie_db.rate = movie.rate
    movie_db.description = movie.description
    movie_db.poster = movie.poster
    movie_db.date_add = movie.date_add

    for genre_id in movie.genres_id:
        genre_db = db.query(m.Genre).filter(m.Genre.id == genre_id).first()
        if genre_db:
            movie_db.genres.append(genre_db)
        else:
            raise HTTPException(status_code=404, detail="Не найдено!")

    db.add(movie_db)
    db.commit()
    return movie_db


@app.delete("/movies/{id}")
def delete_movie(
    id: int, db: Session = Depends(get_db), user: m.User = Depends(basic_auth)
):
    movie = db.query(m.Movie).filter(m.Movie.id == id).first()
    if not movie:
        raise HTTPException(404, "Фильм не найден")
    db.delete(movie)
    db.commit()
    return {"detail": "Фильм удалён"}


@app.get("/genres", response_model=List[pyd.BaseGenre])
def get_all_genres(db: Session = Depends(get_db)):
    genres = db.query(m.Genre).all()
    return genres


@app.post("/genres", response_model=pyd.BaseGenre)
def create_genre(
    genre: pyd.CreateGenre,
    db: Session = Depends(get_db),
    user: m.User = Depends(basic_auth),
):
    genre_db = m.Genre()
    genre_db.genre_name = genre.genre_name
    genre_db.description = genre.description

    db.add(genre_db)
    db.commit()
    return genre_db


@app.put("/movies/{id}", response_model=pyd.SchemeMovie)
def update_movie(
    id: int,
    movie: pyd.CreateMovie,
    db: Session = Depends(get_db),
    user: m.User = Depends(basic_auth),
):
    movie_db = db.query(m.Movie).filter(m.Movie.id == id).first()
    movie_db.movie_name = movie.movie_name
    movie_db.year = movie.year
    movie_db.time = movie.time
    movie_db.rate = movie.rate
    movie_db.description = movie.description
    movie_db.poster = movie.poster
    movie_db.date_add = movie.date_add

    movie_db.genres = []
    for genre_id in movie.genres_id:
        genre_db = db.query(m.Genre).filter(m.Genre.id == genre_id).first()
        if genre_db:
            movie_db.genres.append(genre_db)
        else:
            raise HTTPException(status_code=404, detail="Не найдено!")

    db.add(movie_db)
    db.commit()
    return movie_db


@app.put("/movies/{id}/image", response_model=pyd.SchemeMovie)
def upload_image(
    id: int,
    image: UploadFile,
    db: Session = Depends(get_db),
    user: m.User = Depends(basic_auth),
):
    poster_db = db.query(m.Movie).filter(m.Movie.id == id).first()
    if not poster_db:
        raise HTTPException(404)
    if image.content_type not in ("image/png", "image/jpeg"):
        raise HTTPException(400, "Неверный тип данных")
    if image.size > 5242880:
        raise HTTPException(413, "Файл слишком большой")
    print(image.content_type)
    filename = "".join(random.sample(string.digits + string.ascii_letters, 15))

    files_directory = os.path.join(os.getcwd(), "files")
    if not os.path.exists(files_directory):
        os.makedirs(files_directory)
    with open(f"files/{filename}.{image.content_type[6:]}", "wb+") as f:
        shutil.copyfileobj(image.file, f)
    poster_db.poster = f"files/{filename}.{image.content_type[6:]}"
    db.commit()
    return poster_db
