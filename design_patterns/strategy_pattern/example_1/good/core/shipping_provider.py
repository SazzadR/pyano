import abc


class ShippingProvider(abc.ABC):
    @abc.abstractmethod
    def shipping_cost(self):
        pass


class FEDXShippingProvider(ShippingProvider):
    def shipping_cost(self):
        return 5.00


class UPSShippingProvider(ShippingProvider):
    def shipping_cost(self):
        return 4.00


class PostalShippingProvider(ShippingProvider):
    def shipping_cost(self):
        return 3.00
