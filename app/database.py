from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import settings

# Async Engine for maximum concurrent performance
engine = create_async_engine(settings.DATABASE_URL, echo=False)

# Session factory tailored for FastAPI async injection
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
