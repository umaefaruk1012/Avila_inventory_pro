# models/expense.py
from sqlalchemy import Column, Integer, String, Numeric
from core.database import Base
from core.mixins import TimestampMixin

class Expense(Base, TimestampMixin):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    description = Column(String(255))
    amount = Column(Numeric(12, 2), nullable=False)