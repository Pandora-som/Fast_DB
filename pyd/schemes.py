from .basemodels import *
from typing import List

class SchemeMovie(BaseMovie):
    genres: List[BaseGenre]
    