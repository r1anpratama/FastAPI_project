from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.api.dependencies import get_db
from app.schemas.quote import QuoteResponse
from app.db.models import Quote

router = APIRouter()

@router.get("/", response_model=List[QuoteResponse])
async def read_quotes(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve quotes.
    """
    result = await db.execute(select(Quote).offset(skip).limit(limit))
    quotes = result.scalars().all()
    return quotes

@router.get("/{quote_id}", response_model=QuoteResponse)
async def read_quote(
    quote_id: int, 
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific quote by ID.
    """
    result = await db.execute(select(Quote).filter(Quote.id == quote_id))
    quote = result.scalars().first()
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote
