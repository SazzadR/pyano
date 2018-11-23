from abc import ABCMeta, abstractmethod


class Sub(metaclass=ABCMeta):
    def make(self):
        return self. \
            layout_bread(). \
            add_lettuce(). \
            add_primary_toppings(). \
            add_sauces()

    def layout_bread(self):
        print('laying down the bread')
        return self

    def add_lettuce(self):
        print('add some lettuce')
        return self

    def add_sauces(self):
        print('add oil and vinegar')
        return self

    @abstractmethod
    def add_primary_toppings(self): pass


class TurkeySub(Sub):
    def add_primary_toppings(self):
        print('add some turkey')
        return self


class VeggieSub(Sub):
    def add_primary_toppings(self):
        print('add some veggies')
        return self
