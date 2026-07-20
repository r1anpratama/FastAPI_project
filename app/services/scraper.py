import httpx
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Quote
from app.schemas.quote import QuoteCreate
import asyncio

async def scrape_quotes(session: AsyncSession, pages_to_scrape: int = 1) -> int:
    base_url = "http://quotes.toscrape.com/page/{}/"
    quotes_added = 0
    
    async with httpx.AsyncClient() as client:
        for page in range(1, pages_to_scrape + 1):
            url = base_url.format(page)
            response = await client.get(url)
            
            if response.status_code != 200:
                break
                
            soup = BeautifulSoup(response.text, "html.parser")
            quotes_html = soup.find_all("div", class_="quote")
            
            if not quotes_html:
                break
                
            for quote_html in quotes_html:
                text = quote_html.find("span", class_="text").get_text(strip=True)
                # Remove curly quotes if needed, but keeping as is for authenticity
                author = quote_html.find("small", class_="author").get_text(strip=True)
                tags = [tag.get_text(strip=True) for tag in quote_html.find_all("a", class_="tag")]
                
                tags_str = ",".join(tags)
                
                # Create DB Model
                db_quote = Quote(
                    text=text,
                    author=author,
                    tags=tags_str
                )
                session.add(db_quote)
                quotes_added += 1
                
        # Commit all added quotes to the database
        await session.commit()
        
    return quotes_added
