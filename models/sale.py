# models/sale.py
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Sale(Base, TimestampMixin):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    total_amount = Column(Numeric(14, 2), default=0)

    customer = relationship("Customer", back_populates="sales")
    items = relationship("SaleItem", back_populates="sale")