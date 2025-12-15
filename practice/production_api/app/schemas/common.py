"""
Common schemas for API responses and error handling
"""
from typing import Optional, Any, Dict
from pydantic import BaseModel


class HealthCheck(BaseModel):
    """Schema for health check endpoint response"""
    status: str
    version: str
    environment: str
    database: str = "ok"
    redis: str = "ok"


class ErrorResponse(BaseModel):
    """Schema for error responses"""
    detail: str
    error_code: Optional[str] = None
    timestamp: Optional[str] = None


class SuccessResponse(BaseModel):
    """Schema for generic success responses"""
    message: str
    data: Optional[Dict[str, Any]] = None


class PaginationParams(BaseModel):
    """Schema for pagination parameters"""
    skip: int = 0
    limit: int = 100


class PaginatedResponse(BaseModel):
    """Schema for paginated responses"""
    items: list
    total: int
    skip: int
    limit: int
    has_more: bool
