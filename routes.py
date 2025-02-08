from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Product, Supplier

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products")
def get_products(brand: str, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.brand == brand).all()

@router.get("/suppliers")
def get_suppliers(category: str, db: Session = Depends(get_db)):
    return db.query(Supplier).filter(Supplier.product_categories.ilike(f"%{category}%")).all()
