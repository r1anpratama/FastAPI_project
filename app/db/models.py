from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    author = Column(String(255), nullable=False)
    tags = Column(String(500), nullable=True) # Storing tags as comma-separated string for simplicity
