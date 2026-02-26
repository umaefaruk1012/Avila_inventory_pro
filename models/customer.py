# models/customer.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Customer(Base, TimestampMixin):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(50))
    email = Column(String(100))

    sales = relationship("Sale", back_populates="customer")