from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.routers import products

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (In production, use Alembic migrations instead)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Clean up resources on shutdown
    await engine.dispose()

app = FastAPI(
    title="Store Inventory API",
    description="A classic, production-ready REST API demonstrating CRUD, SQLAlchemy, and PostgreSQL.",
    version="1.0.0",
    lifespan=lifespan
)

# Include the routers
app.include_router(products.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}
