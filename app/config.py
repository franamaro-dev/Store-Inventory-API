from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Store Inventory API"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/inventory_db"

    class Config:
        env_file = ".env"

settings = Settings()
