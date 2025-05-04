from enum import Enum
from functools import lru_cache
from typing import Optional

from decouple import config as decouple_config
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # Environment settings
    ENVIRONMENT: EnvironmentType = Field(
        default=EnvironmentType.DEVELOPMENT,
        description="The environment the application is running in",
    )
    DEBUG: bool = Field(default=True, description="Debug mode flag")

    # API Keys
    OPENAI_API_KEY: str = Field(description="OpenAI API key (optional)")
    ANTHROPIC_API_KEY: Optional[str] = Field(
        default=None, description="Anthropic API key (optional)"
    )
    GEMINI_API_KEY: Optional[str] = Field(
        default=None, description="Gemini API key (optional)"
    )

    # Local LLM settings
    AVAILABLE_LOCAL_LLM_MODELS: list[str] = Field(
        default=[], description="Available local LLM models"
    )
    LM_STUDIO_HOST: Optional[str] = Field(
        default="localhost", description="Local LLM host (optional)"
    )
    LM_STUDIO_PORT: Optional[int] = Field(
        default="1234", description="Local LLM port (optional)"
    )

    # Application settings
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    MAX_TOKENS: int = Field(
        default=4096, description="Maximum tokens for LLM responses"
    )
    TEMPERATURE: float = Field(default=0.7, description="Temperature for LLM responses")

    # Add other configuration as needed


@lru_cache()
def get_settings() -> Settings:
    """
    Get application settings with caching to avoid reading the environment
    variables multiple times. Use this function to access settings.

    Example:
        settings = get_settings()
        api_key = settings.OPENAI_API_KEY
    """
    return Settings()
