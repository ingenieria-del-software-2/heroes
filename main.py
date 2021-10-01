from sqlmodel import Session, select
from fastapi import FastAPI, HTTPException
from model import engine, Hero
import httpx
import os

app = FastAPI()


@app.get("/heroes")
def list_all_heroes():
    with Session(engine) as session:
        return list(session.exec(select(Hero)))


USERS_HOST = os.getenv("USERS_HOST", "")


@app.post("/heroes", status_code=201, response_model=Hero)
def create_hero(hero: Hero):
    creator = httpx.get(f"{USERS_HOST}/{hero.author}")
    if creator.status_code != 200:
        raise HTTPException(status_code=404, detail="Author not found")

    print(hero)
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
