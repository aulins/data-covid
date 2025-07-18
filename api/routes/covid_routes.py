from fastapi import APIRouter
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


@router.get("/")
def home():
    return {"message": "API COVID Siap!"}


@router.get("/covid")
def get_all_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM covid_stats")).mappings()
        data = [dict(row) for row in result]
    return data


@router.get("/covid/{country}")
def get_by_country(country: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM covid_stats WHERE country ILIKE :country"),
            {"country": country}
        ).mappings()
        data = [dict(row) for row in result]
    return data


@router.get("/covid/indonesia")
def get_indonesia_data():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT tanggal, kasus_baru, sembuh, meninggal
            FROM covid_stats
            WHERE country ILIKE 'Indonesia'
            ORDER BY tanggal
        """)).mappings()
        return [dict(row) for row in result]

@router.get("/covid/indonesia/detail")
def get_indonesia_detail():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT tanggal, kasus_baru, sembuh, meninggal
            FROM covid_stats
            WHERE country ILIKE 'Indonesia'
            ORDER BY tanggal
        """)).mappings()
        return [dict(row) for row in result]
