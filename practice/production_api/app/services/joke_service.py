"""
Joke service for fetching and managing jokes
Implements caching and external API integration
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
import httpx
from fastapi import HTTPException, status

from app.models.joke import Joke
from app.schemas.joke import JokeCreate, JokeSimpleResponse
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class JokeService:
    """Service for joke-related operations"""
    
    @staticmethod
    async def fetch_joke_from_api() -> JokeSimpleResponse:
        """
        Fetch a random joke from external API
        
        Returns:
            JokeSimpleResponse with joke data
            
        Raises:
            HTTPException: If API request fails
        """
        try:
            async with httpx.AsyncClient(timeout=settings.API_TIMEOUT) as client:
                response = await client.get(f"{settings.JOKE_API_URL}/random_joke")
                response.raise_for_status()
                
                joke_data = response.json()
                logger.info("Joke fetched from API", joke_id=joke_data.get("id"))
                
                return JokeSimpleResponse(
                    setup=joke_data["setup"],
                    punchline=joke_data["punchline"],
                    type=joke_data.get("type")
                )
        except httpx.HTTPError as e:
            logger.error("Failed to fetch joke from API", error=str(e))
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Could not fetch joke from external service"
            )
    
    @staticmethod
    async def save_joke(db: AsyncSession, joke_data: JokeSimpleResponse) -> Joke:
        """
        Save a joke to the database
        
        Args:
            db: Database session
            joke_data: Joke data to save
            
        Returns:
            Saved joke
        """
        db_joke = Joke(
            setup=joke_data.setup,
            punchline=joke_data.punchline,
            joke_type=joke_data.type,
            source="official-joke-api"
        )
        
        db.add(db_joke)
        await db.commit()
        await db.refresh(db_joke)
        
        logger.info("Joke saved to database", joke_id=db_joke.id)
        return db_joke
    
    @staticmethod
    async def get_random_cached_joke(db: AsyncSession) -> Optional[Joke]:
        """
        Get a random joke from the database cache
        
        Args:
            db: Database session
            
        Returns:
            Random joke or None if cache is empty
        """
        result = await db.execute(
            select(Joke).order_by(func.random()).limit(1)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_joke(db: AsyncSession, use_cache: bool = True) -> JokeSimpleResponse:
        """
        Get a joke, using cache if available and requested
        
        Args:
            db: Database session
            use_cache: Whether to try cache first
            
        Returns:
            JokeSimpleResponse
        """
        # Try cache first if enabled
        if use_cache:
            cached_joke = await JokeService.get_random_cached_joke(db)
            if cached_joke:
                logger.info("Returning cached joke", joke_id=cached_joke.id)
                return JokeSimpleResponse(
                    setup=cached_joke.setup,
                    punchline=cached_joke.punchline,
                    type=cached_joke.joke_type
                )
        
        # Fetch from API
        joke = await JokeService.fetch_joke_from_api()
        
        # Save to cache (fire and forget)
        try:
            await JokeService.save_joke(db, joke)
        except Exception as e:
            logger.warning("Failed to cache joke", error=str(e))
        
        return joke
    
    @staticmethod
    async def get_jokes(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100
    ) -> List[Joke]:
        """
        Get list of cached jokes with pagination
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of jokes
        """
        result = await db.execute(
            select(Joke).offset(skip).limit(limit).order_by(Joke.created_at.desc())
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_joke_by_id(db: AsyncSession, joke_id: int) -> Optional[Joke]:
        """
        Get a specific joke by ID
        
        Args:
            db: Database session
            joke_id: Joke ID
            
        Returns:
            Joke or None if not found
        """
        result = await db.execute(select(Joke).where(Joke.id == joke_id))
        return result.scalar_one_or_none()
