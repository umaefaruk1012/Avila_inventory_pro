import pytest
from models.product import Product
from services.purchase_service import PurchaseService


def test_purchase_increases_stock(db):
    product = Product(
        name="New Product",
        sku="NEW001",
        cost_price=10,
        selling_price=20,
        quantity_in_stock=5,
    )
    db.add(product)
    db.commit()

    PurchaseService.create_purchase(
        db,
        supplier_id=None,
        items=[{"product_id": product.id, "quantity": 10, "unit_cost": 8}],
    )

    updated_product = db.query(Product).filter_by(id=product.id).first()
    assert updated_product.quantity_in_stock == 15