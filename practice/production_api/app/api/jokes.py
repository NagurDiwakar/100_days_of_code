"""
Joke API endpoints
Handles joke fetching and management
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.joke import JokeSimpleResponse, JokeResponse
from app.services.joke_service import JokeService
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get("/random", response_model=JokeSimpleResponse)
async def get_random_joke(
    use_cache: bool = Query(True, description="Use cached jokes if available"),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a random joke
    
    - **use_cache**: If true, may return a cached joke (faster). If false, always fetches from external API.
    
    Returns a random joke with setup and punchline
    """
    joke = await JokeService.get_joke(db, use_cache=use_cache)
    logger.info("Random joke served")
    return joke


@router.get("/", response_model=List[JokeResponse])
async def list_jokes(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    """
    List all cached jokes with pagination
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100, max: 100)
    """
    jokes = await JokeService.get_jokes(db, skip=skip, limit=limit)
    return jokes


@router.get("/{joke_id}", response_model=JokeResponse)
async def get_joke_by_id(
    joke_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific joke by ID
    
    - **joke_id**: The ID of the joke to retrieve
    """
    joke = await JokeService.get_joke_by_id(db, joke_id)
    if not joke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Joke not found"
        )
    return joke
