class Order(object):
    def __init__(self, shipping_provider):
        self._shipping_provider = shipping_provider

    @property
    def shipping_provider(self):
        return self._shipping_provider
