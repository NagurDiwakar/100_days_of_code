"""
Joke model for storing fetched jokes
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.db.session import Base


class Joke(Base):
    """Joke model for caching jokes"""
    
    __tablename__ = "jokes"
    
    id = Column(Integer, primary_key=True, index=True)
    setup = Column(Text, nullable=False)
    punchline = Column(Text, nullable=False)
    joke_type = Column(String, nullable=True)
    source = Column(String, default="official-joke-api")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Joke(id={self.id}, type={self.joke_type})>"
