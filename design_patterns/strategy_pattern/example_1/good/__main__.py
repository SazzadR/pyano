from core import Order, FEDXShippingProvider, UPSShippingProvider, PostalShippingProvider

fedx = FEDXShippingProvider()
order = Order(shipping_provider=fedx)
cost = order.shipping_cost()
assert cost == 5.00

ups = UPSShippingProvider()
order = Order(shipping_provider=ups)
cost = order.shipping_cost()
assert cost == 4.00

postal = PostalShippingProvider()
order = Order(shipping_provider=postal)
cost = order.shipping_cost()
assert cost == 3.00

print("All test passes!")
