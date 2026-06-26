from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Job Intelligence Platform"

    DATABASE_URL: str

    LOG_LEVEL: str = "INFO"

    email_address: str
    email_password: str
    email_to: str

    telegram_token: str
    telegram_chat_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"   # or "forbid" if you want strict validation
    )

settings = Settings()