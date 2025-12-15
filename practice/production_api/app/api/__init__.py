"""API router initialization"""
from fastapi import APIRouter
from app.api import auth, users, jokes, health

# Create main API router
api_router = APIRouter()

# Include all sub-routers
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(jokes.router)

__all__ = ["api_router"]
