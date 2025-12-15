"""
Authentication API endpoints
Handles user registration, login, and token management
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, LoginRequest, Token
from app.services.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new user
    
    - **email**: Valid email address
    - **username**: Unique username (3-50 characters)
    - **password**: Password (min 8 characters)
    - **full_name**: Optional full name
    """
    user = await UserService.create_user(db, user_data)
    logger.info("User registered successfully", user_id=user.id)
    return user


@router.post("/login", response_model=Token)
async def login(
    login_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Login and receive access and refresh tokens
    
    - **username**: Username or email
    - **password**: User password
    """
    user = await UserService.authenticate_user(
        db, 
        login_data.username, 
        login_data.password
    )
    
    if not user:
        logger.warning("Failed login attempt", username=login_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create tokens
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id}
    )
    refresh_token = create_refresh_token(
        data={"sub": user.username, "user_id": user.id}
    )
    
    logger.info("User logged in successfully", user_id=user.id)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Refresh access token using refresh token
    
    Requires valid refresh token in Authorization header
    """
    # Verify token type
    if current_user.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type"
        )
    
    # Create new tokens
    access_token = create_access_token(
        data={"sub": current_user["sub"], "user_id": current_user["user_id"]}
    )
    refresh_token = create_refresh_token(
        data={"sub": current_user["sub"], "user_id": current_user["user_id"]}
    )
    
    logger.info("Token refreshed", user_id=current_user["user_id"])
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
