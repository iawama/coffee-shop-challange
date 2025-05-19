import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initializer_and_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    customer.name = "Bob"
    assert customer.name == "Bob"

def test_customer_relationships():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order in customer.orders()
    assert coffee in customer.coffees()
    assert len(customer.coffees()) == 1  # Unique coffees

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_most_aficionado():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 6.0)
    Order(customer1, coffee, 3.0)
    assert Customer.most_aficionado(coffee) == customer1  # 8.0 vs 6.0
    coffee2 = Coffee("Espresso")
    assert Customer.most_aficionado(coffee2) is None