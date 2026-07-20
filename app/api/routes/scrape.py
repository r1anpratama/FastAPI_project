from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.services.scraper import scrape_quotes

router = APIRouter()

@router.post("/run")
async def run_scraper(
    pages: int = 1,
    db: AsyncSession = Depends(get_db)
):
    """
    Trigger the scraper to fetch quotes and save them to the database.
    """
    quotes_added = await scrape_quotes(session=db, pages_to_scrape=pages)
    return {"message": f"Successfully scraped and added {quotes_added} quotes."}
