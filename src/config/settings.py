from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    OPENAI_API_KEY: str

    model_config = ConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
