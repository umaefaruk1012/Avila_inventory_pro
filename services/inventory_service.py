from sqlalchemy.orm import Session
from models.product import Product
from models.stock_movement import StockMovement
from exceptions.business_exceptions import (
    InsufficientStockError,
    ProductNotFoundError,
)


class InventoryService:

    @staticmethod
    def increase_stock(db: Session, product_id: int, quantity: int, movement_type="PURCHASE"):
        product = db.query(Product).filter_by(id=product_id).first()

        if not product:
            raise ProductNotFoundError()

        product.quantity_in_stock += quantity

        movement = StockMovement(
            product_id=product_id,
            quantity=quantity,
            movement_type=movement_type,
        )

        db.add(movement)

    @staticmethod
    def decrease_stock(db: Session, product_id: int, quantity: int, movement_type="SALE"):
        product = db.query(Product).filter_by(id=product_id).first()

        if not product:
            raise ProductNotFoundError()

        if product.quantity_in_stock < quantity:
            raise InsufficientStockError(
                f"Available: {product.quantity_in_stock}, Requested: {quantity}"
            )

        product.quantity_in_stock -= quantity

        movement = StockMovement(
            product_id=product_id,
            quantity=-quantity,
            movement_type=movement_type,
        )

        db.add(movement)