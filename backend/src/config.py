# Настройки приложения

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list[
        "http://0.0.0.0:8000",
        "http://localhost:8000",
        "http://localhost:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        model_config = SettingsConfigDict(env_file=".env")
        
settings = Settings()