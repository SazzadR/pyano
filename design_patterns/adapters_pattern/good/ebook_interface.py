from abc import ABCMeta, abstractmethod


class EBookInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self): pass

    @abstractmethod
    def press_next_button(self): pass
