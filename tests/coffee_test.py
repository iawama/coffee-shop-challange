import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initializer_and_name():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Ab")
    with pytest.raises(AttributeError):
        coffee.name = "Espresso"

def test_coffee_relationships():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 5.0)
    assert order in coffee.orders()
    assert customer in coffee.customers()
    assert len(coffee.customers()) == 1  # Unique customers

def test_coffee_aggregates():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 7.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0
    coffee2 = Coffee("Espresso")
    assert coffee2.num_orders() == 0
    assert coffee2.average_price() == 0