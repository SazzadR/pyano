from .shipping_provider import ShippingProvider


class ShippingCost(object):
    def cost(self, order):
        if order.shipping_provider == ShippingProvider.fedx:
            return self._fedx_cost(order)
        elif order.shipping_provider == ShippingProvider.ups:
            return self._ups_cost(order)
        elif order.shipping_provider == ShippingProvider.postal:
            return self._postal_cost(order)
        else:
            raise ValueError("Invalid shipping provider %s", order.shipping_provider)

    def _fedx_cost(self, order):
        return 5.00

    def _ups_cost(self, order):
        return 4.00

    def _postal_cost(self, order):
        return 3.00
