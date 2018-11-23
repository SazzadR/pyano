from abc import ABCMeta, abstractmethod


class BookInterface(metaclass=ABCMeta):
    @abstractmethod
    def open(self): pass

    @abstractmethod
    def turn_page(self): pass
