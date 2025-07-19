from fastapi import FastAPI
from api.routes import covid_routes
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# Daftarkan router dari routes
app.include_router(covid_routes.router)
