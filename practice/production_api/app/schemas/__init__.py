"""Schemas initialization"""
from app.schemas.user import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserInDB,
    UserResponse,
    Token,
    TokenData,
    LoginRequest,
)
from app.schemas.joke import (
    JokeBase,
    JokeCreate,
    JokeResponse,
    JokeSimpleResponse,
)
from app.schemas.common import (
    HealthCheck,
    ErrorResponse,
    SuccessResponse,
    PaginationParams,
    PaginatedResponse,
)

__all__ = [
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserInDB",
    "UserResponse",
    "Token",
    "TokenData",
    "LoginRequest",
    "JokeBase",
    "JokeCreate",
    "JokeResponse",
    "JokeSimpleResponse",
    "HealthCheck",
    "ErrorResponse",
    "SuccessResponse",
    "PaginationParams",
    "PaginatedResponse",
]
