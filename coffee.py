from order import Order

class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name  # Use setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Coffee name cannot be changed after initialization")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    def orders(self):
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0