from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    order_id: int
    customer_id: int
    order_status: int
    order_date: datetime
    required_date: datetime
    shipped_date: datetime
    store_id: int
    staff_id: int

    # Altri campi corrispondenti alla tabella

    def __hash__(self):
        return hash(self.order_id)

    def __str__(self):
        return str(self.order_id)

    def __repr__(self):
        return self.order_id