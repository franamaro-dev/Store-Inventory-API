from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products Inventory"]
)

@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)):
    """Create a new product in the inventory."""
    return await crud.create_product(db=db, product=product)

@router.get("/", response_model=List[schemas.ProductResponse])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """Retrieve a list of products."""
    products = await crud.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=schemas.ProductResponse)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve a specific product by its ID."""
    db_product = await crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=schemas.ProductResponse)
async def update_product(product_id: int, product: schemas.ProductUpdate, db: AsyncSession = Depends(get_db)):
    """Update a product's details or stock."""
    db_product = await crud.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Remove a product from the inventory."""
    success = await crud.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
