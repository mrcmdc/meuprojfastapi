from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8', env_file='.env'
    )
    DATABASE_URL: str
