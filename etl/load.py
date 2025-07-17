import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load variabel dari .env
load_dotenv()

# Ambil koneksi database dari environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Cek jika DATABASE_URL tidak ditemukan
if not DATABASE_URL:
    raise ValueError("DATABASE_URL tidak ditemukan di file .env")

# Buat koneksi engine PostgreSQL
engine = create_engine(DATABASE_URL)

# Baca CSV
df = pd.read_csv('data/cleaned/covid_cleaned.csv')

# Simpan ke PostgreSQL
df.to_sql("covid_stats", con=engine, if_exists='replace', index=False)

print("✅ Data berhasil dimuat ke tabel 'covid_stats'")
