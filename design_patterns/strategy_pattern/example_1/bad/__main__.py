from core import Order, ShippingProvider, ShippingCost

order = Order(ShippingProvider.fedx)
shipping_cost = ShippingCost()
cost = shipping_cost.cost(order)
assert cost == 5.0

order = Order(ShippingProvider.ups)
shipping_cost = ShippingCost()
cost = shipping_cost.cost(order)
assert cost == 4.0

order = Order(ShippingProvider.postal)
shipping_cost = ShippingCost()
cost = shipping_cost.cost(order)
assert cost == 3.0

print("All test passes!")
