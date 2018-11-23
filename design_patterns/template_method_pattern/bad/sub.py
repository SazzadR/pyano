class TurkeySub:
    def make(self):
        return self. \
            layout_bread(). \
            add_lettuce(). \
            add_turkey(). \
            add_sauces()

    def layout_bread(self):
        print('laying down the bread')
        return self

    def add_lettuce(self):
        print('add some lettuce')
        return self

    def add_turkey(self):
        print('add some turkey')
        return self

    def add_sauces(self):
        print('add oil and vinegar')
        return self


class VeggieSub:
    def make(self):
        return self. \
            layout_bread(). \
            add_lettuce(). \
            add_veggies(). \
            add_sauces()

    def layout_bread(self):
        print('laying down the bread')
        return self

    def add_lettuce(self):
        print('add some lettuce')
        return self

    def add_veggies(self):
        print('add some veggies')
        return self

    def add_sauces(self):
        print('add oil and vinegar')
        return self
