import pytest
from models.product import Product
from services.inventory_service import InventoryService
from exceptions.business_exceptions import InsufficientStockError, ProductNotFoundError


def test_inventory_increase_stock(db):
    product = Product(
        name="Stock Product",
        sku="STK001",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=0,
    )
    db.add(product)
    db.commit()

    InventoryService.increase_stock(db, product_id=product.id, quantity=5)
    db.commit()

    updated_product = db.query(Product).filter_by(id=product.id).first()
    assert updated_product.quantity_in_stock == 5


def test_inventory_decrease_stock(db):
    product = Product(
        name="Stock Product",
        sku="STK002",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=10,
    )
    db.add(product)
    db.commit()

    InventoryService.decrease_stock(db, product_id=product.id, quantity=3)
    db.commit()

    updated_product = db.query(Product).filter_by(id=product.id).first()
    assert updated_product.quantity_in_stock == 7


def test_inventory_decrease_stock_not_enough(db):
    product = Product(
        name="Stock Product",
        sku="STK003",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=2,
    )
    db.add(product)
    db.commit()

    with pytest.raises(InsufficientStockError):
        InventoryService.decrease_stock(db, product_id=product.id, quantity=5)


def test_inventory_product_not_found(db):
    with pytest.raises(ProductNotFoundError):
        InventoryService.decrease_stock(db, product_id=9999, quantity=1)