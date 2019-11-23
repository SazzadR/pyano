import abc


class EC2Observer(abc.ABC):
    @abc.abstractmethod
    def handle(self):
        pass
