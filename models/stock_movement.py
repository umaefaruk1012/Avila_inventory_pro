# models/stock_movement.py
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class StockMovement(Base, TimestampMixin):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    movement_type = Column(String(50))  # PURCHASE, SALE, ADJUSTMENT

    product = relationship("Product", back_populates="stock_movements")