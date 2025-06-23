from pydantic_settings import BaseSettings, SettingsConfigDict
import secrets

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    # App
    API_V1_STR: str = "/api/v1"

    # JWT
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 ngày
    ALGORITHM: str = "HS256"

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/your-agents"


settings = Settings()  # type: ignore