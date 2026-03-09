from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Store Inventory API"
    SECRET_KEY: str = "your-secret-key-for-jwt-development" # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/inventory_db"

    class Config:
        env_file = ".env"

settings = Settings()
