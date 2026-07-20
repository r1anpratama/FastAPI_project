from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class QuoteBase(BaseModel):
    text: str
    author: str
    tags: Optional[str] = None

class QuoteCreate(QuoteBase):
    pass

class QuoteResponse(QuoteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
