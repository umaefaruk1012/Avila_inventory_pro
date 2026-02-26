# models/category.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.mixins import TimestampMixin

class Category(Base, TimestampMixin):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    products = relationship("Product", back_populates="category")