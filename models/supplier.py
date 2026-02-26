# models/supplier.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Supplier(Base, TimestampMixin):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(50))
    address = Column(String(255))

    purchases = relationship("Purchase", back_populates="supplier")