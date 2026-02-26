from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.purchase import Purchase
from models.purchase_item import PurchaseItem
from services.inventory_service import InventoryService


class PurchaseService:

    @staticmethod
    def create_purchase(db: Session, supplier_id: int, items: list):
        try:
            purchase = Purchase(supplier_id=supplier_id)
            db.add(purchase)

            total = 0

            for item in items:
                line_total = item["unit_cost"] * item["quantity"]
                total += line_total

                purchase_item = PurchaseItem(
                    purchase=purchase,
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                    unit_cost=item["unit_cost"],
                )

                db.add(purchase_item)

                InventoryService.increase_stock(
                    db,
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                )

            purchase.total_amount = total

            db.commit()
            db.refresh(purchase)

            return purchase

        except SQLAlchemyError:
            db.rollback()
            raise