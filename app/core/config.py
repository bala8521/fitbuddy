import os
from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central application settings loaded from environment variables or .env file."""

    APP_NAME: str = "FitBuddy"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    SECRET_KEY: str = "fitbuddy-dev-secret-key-change-in-production-1234567890"

    # Database
    DATABASE_URL: str = "sqlite:///./fitbuddy.db"

    # Google Gemini AI Settings
    GEMINI_API_KEY: Optional[str] = None
    GEMINI_WORKOUT_MODEL: str = "gemini-2.5-flash"
    GEMINI_FAST_MODEL: str = "gemini-2.5-flash"

    # Admin Credentials
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "adminpassword123"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Returns cached settings instance."""
    return Settings()
