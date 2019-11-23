from .shipping_provider import ShippingProvider


class Order(object):
    def __init__(self, shipping_provider: ShippingProvider):
        self.shipping_provider = shipping_provider

    def shipping_cost(self):
        return self.shipping_provider.shipping_cost()
