from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.sale import Sale
from models.sale_item import SaleItem
from models.product import Product
from services.inventory_service import InventoryService


class SaleService:

    @staticmethod
    def create_sale(db: Session, customer_id: int, items: list):
        try:
            sale = Sale(customer_id=customer_id)
            db.add(sale)

            total = 0

            for item in items:
                product = db.query(Product).filter_by(
                    id=item["product_id"]
                ).with_for_update().first()

                if not product:
                    raise Exception("Product not found")

                line_total = product.selling_price * item["quantity"]
                total += line_total

                sale_item = SaleItem(
                    sale=sale,
                    product_id=product.id,
                    quantity=item["quantity"],
                    unit_price=product.selling_price,
                )

                db.add(sale_item)

                InventoryService.decrease_stock(
                    db,
                    product_id=product.id,
                    quantity=item["quantity"],
                )

            sale.total_amount = total

            db.commit()
            db.refresh(sale)

            return sale

        except SQLAlchemyError:
            db.rollback()
            raise