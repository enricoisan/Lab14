from dataclasses import dataclass

@dataclass
class Store:
    store_id: int
    store_name: float
    phone: float
    email: float
    street: float
    city: float
    state: float
    zip_code: int

    def __hash__(self):
        return hash(self.store_id)

    def __str__(self):
        return str(self.store_id)

    def __repr__(self):
        return self.store_name