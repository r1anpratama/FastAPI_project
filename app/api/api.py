from fastapi import APIRouter
from app.api.routes import quotes, scrape

api_router = APIRouter()
api_router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
api_router.include_router(scrape.router, prefix="/scrape", tags=["scrape"])
