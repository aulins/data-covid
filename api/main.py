from fastapi import FastAPI
from api.routes import covid_routes
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# Daftarkan router dari routes
app.include_router(covid_routes.router)


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Tambahkan baris ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ubah ke domain spesifik jika produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
