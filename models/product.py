# models/product.py
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Product(Base, TimestampMixin):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    sku = Column(String(100), unique=True, nullable=False)

    cost_price = Column(Numeric(12, 2), nullable=False)
    selling_price = Column(Numeric(12, 2), nullable=False)

    quantity_in_stock = Column(Integer, default=0)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    stock_movements = relationship("StockMovement", back_populates="product")