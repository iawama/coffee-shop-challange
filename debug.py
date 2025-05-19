from customer import Customer
from coffee import Coffee
from order import Order

# Create test data
customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer1.create_order(coffee2, 3.0)
order3 = customer2.create_order(coffee1, 6.0)

# Test relationships
print(f"{customer1.name}'s orders: {[order.price for order in customer1.orders()]}")
print(f"{customer1.name}'s coffees: {[coffee.name for coffee in customer1.coffees()]}")
print(f"{coffee1.name}'s orders: {[order.price for order in coffee1.orders()]}")
print(f"{coffee1.name}'s customers: {[customer.name for customer in coffee1.customers()]}")
print(f"Number of orders for {coffee1.name}: {coffee1.num_orders()}")
print(f"Average price for {coffee1.name}: {coffee1.average_price()}")

# Test bonus
most_aficionado = Customer.most_aficionado(coffee1)
print(f"Most aficionado for {coffee1.name}: {most_aficionado.name if most_aficionado else None}")