import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initializer_and_properties():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    with pytest.raises(TypeError):
        Order("Not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(customer, "Not a coffee", 5.0)
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)
    with pytest.raises(AttributeError):
        order.price = 6.0