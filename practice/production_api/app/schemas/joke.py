"""
Pydantic schemas for joke-related requests and responses
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class JokeBase(BaseModel):
    """Base joke schema"""
    setup: str = Field(..., min_length=1)
    punchline: str = Field(..., min_length=1)
    joke_type: Optional[str] = None


class JokeCreate(JokeBase):
    """Schema for creating a joke"""
    source: Optional[str] = "official-joke-api"


class JokeResponse(JokeBase):
    """Schema for joke response"""
    id: int
    source: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class JokeSimpleResponse(BaseModel):
    """Simplified joke response for API endpoints"""
    setup: str
    punchline: str
    type: Optional[str] = None
