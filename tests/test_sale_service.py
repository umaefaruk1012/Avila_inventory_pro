import pytest
from models.product import Product
from services.sales_service import SaleService
from exceptions.business_exceptions import InsufficientStockError


def test_sale_reduces_stock(db):
    product = Product(
        name="Test Product",
        sku="TEST001",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=10,
    )
    db.add(product)
    db.commit()

    SaleService.create_sale(
        db,
        customer_id=None,
        items=[{"product_id": product.id, "quantity": 2}],
    )

    updated_product = db.query(Product).filter_by(id=product.id).first()
    assert updated_product.quantity_in_stock == 8


def test_sale_fails_if_not_enough_stock(db):
    product = Product(
        name="Limited Product",
        sku="LIMIT001",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=1,
    )
    db.add(product)
    db.commit()

    with pytest.raises(InsufficientStockError):
        SaleService.create_sale(
            db,
            customer_id=None,
            items=[{"product_id": product.id, "quantity": 5}],
        )