from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración central de la aplicación."""

    # Database
    DATABASE_URL: str = "sqlite:///./pySigHor.db"

    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "pySigHor"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
