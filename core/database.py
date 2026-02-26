import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=1800,
    echo=False
)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    from models import (
        user,
        role,
        category,
        supplier,
        customer,
        product,
        stock_movement,
        purchase,
        purchase_item,
        sale,
        sale_item,
        expense,
    )
    Base.metadata.create_all(bind=engine)
