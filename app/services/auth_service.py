from sqlalchemy.orm import Session
from datetime import timedelta
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories import user_repository
from app.core.config import settings


def register_user(db: Session, data: UserCreate) -> str:
    if user_repository.get_by_email(db, data.email):
        raise ValueError("Email already registered")

    user = User(
        email=data.email,
        full_name=data.full_name,
        hashed_password=hash_password(data.password)
    )
    user_repository.create(db, user)

    return create_access_token(user.email, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))


def login_user(db: Session, data: UserLogin) -> str:
    user = user_repository.get_by_email(db, data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise ValueError("Invalid credentials")

    return create_access_token(user.email, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))