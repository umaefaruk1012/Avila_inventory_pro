import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base

# --- Ensure all models are imported ---
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

# --- Setup test database ---
TEST_DATABASE_URL = "postgresql+psycopg2://postgres:AvilaIT@localhost:5432/test_inventory"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def db():
    # All tables now known to metadata
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)