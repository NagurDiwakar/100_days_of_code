"""
Business logic services
Separates business logic from API endpoints for better testability and maintainability
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from app.core.logging import get_logger

logger = get_logger(__name__)


class UserService:
    """Service for user-related operations"""
    
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        """Get user by ID"""
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
        """Get user by email"""
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_username(db: AsyncSession, username: str) -> Optional[User]:
        """Get user by username"""
        result = await db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_users(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[User]:
        """Get list of users with pagination"""
        result = await db.execute(
            select(User).offset(skip).limit(limit).order_by(User.created_at.desc())
        )
        return result.scalars().all()
    
    @staticmethod
    async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
        """
        Create a new user
        
        Args:
            db: Database session
            user_data: User creation data
            
        Returns:
            Created user
            
        Raises:
            HTTPException: If user already exists
        """
        # Check if user already exists
        existing_user = await UserService.get_user_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        existing_username = await UserService.get_user_by_username(db, user_data.username)
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )
        
        # Create user
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
        )
        
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        
        logger.info("User created", user_id=db_user.id, username=db_user.username)
        return db_user
    
    @staticmethod
    async def update_user(
        db: AsyncSession, 
        user_id: int, 
        user_data: UserUpdate
    ) -> User:
        """
        Update user information
        
        Args:
            db: Database session
            user_id: User ID to update
            user_data: Updated user data
            
        Returns:
            Updated user
            
        Raises:
            HTTPException: If user not found
        """
        user = await UserService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Update fields
        update_data = user_data.model_dump(exclude_unset=True)
        
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
        
        for field, value in update_data.items():
            setattr(user, field, value)
        
        await db.commit()
        await db.refresh(user)
        
        logger.info("User updated", user_id=user.id)
        return user
    
    @staticmethod
    async def authenticate_user(
        db: AsyncSession, 
        username: str, 
        password: str
    ) -> Optional[User]:
        """
        Authenticate user with username and password
        
        Args:
            db: Database session
            username: Username or email
            password: Plain text password
            
        Returns:
            User if authentication successful, None otherwise
        """
        # Try to find user by username or email
        user = await UserService.get_user_by_username(db, username)
        if not user:
            user = await UserService.get_user_by_email(db, username)
        
        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        if not user.is_active:
            return None
        
        logger.info("User authenticated", user_id=user.id, username=user.username)
        return user
    
    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> bool:
        """
        Delete a user
        
        Args:
            db: Database session
            user_id: User ID to delete
            
        Returns:
            True if deleted successfully
            
        Raises:
            HTTPException: If user not found
        """
        user = await UserService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        await db.delete(user)
        await db.commit()
        
        logger.info("User deleted", user_id=user_id)
        return True
