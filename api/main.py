from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import covid_routes
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# Daftarkan router dari routes


from fastapi.middleware.cors import CORSMiddleware



# Tambahkan middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ubah ke domain spesifik jika produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pasang router
app.include_router(covid_routes.router)