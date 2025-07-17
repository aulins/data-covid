from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:bismillah@localhost:5432/covid_data")
engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "API COVID Siap!"}

@app.get("/covid")
def get_all_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM covid_stats")).mappings()
        data = [dict(row) for row in result]
    return data


@app.get("/covid/{country}")
def get_by_country(country: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM covid_stats WHERE country ILIKE :country"),
            {"country": country}
        ).mappings()
        data = [dict(row) for row in result]
    return data

