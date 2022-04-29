
    # name: Danna Villamil
    # date: 04/04/2022
    # https://www.youtube.com/watch?v=4e2VW3Nu-64&ab_channel=FaztCode

from fastapi import FastAPI
from routes.superhero import superhero
from config.db import conn

app = FastAPI()

app.include_router(superhero)
