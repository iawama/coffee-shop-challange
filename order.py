class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer  # Use setter for validation
        self.coffee = coffee      # Use setter for validation
        self.price = price        # Use setter for validation
        Order._all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price') and self._price is not None:
            raise AttributeError("Price cannot be changed after initialization")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value