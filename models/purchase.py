# models/purchase.py
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Purchase(Base, TimestampMixin):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)

    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    total_amount = Column(Numeric(14, 2), default=0)

    supplier = relationship("Supplier", back_populates="purchases")
    items = relationship("PurchaseItem", back_populates="purchase")