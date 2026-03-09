from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.routers import products, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    # In production, we use Alembic migrations instead of Base.metadata.create_all
    yield
    # Clean up resources on shutdown
    await engine.dispose()

app = FastAPI(
    title="Store Inventory API",
    description="A classic, production-ready REST API with Auth & Migrations.",
    version="1.1.0",
    lifespan=lifespan
)

# Include the routers
app.include_router(auth.router)
app.include_router(products.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}
