from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd

app=FastAPI()

@app.get('/movies', response_model=List[pyd.BaseMovie])
def get_all_movies(db:Session=Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies