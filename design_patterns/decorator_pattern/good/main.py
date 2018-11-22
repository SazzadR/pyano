from abc import ABCMeta, abstractmethod


class CarService(metaclass=ABCMeta):
    @abstractmethod
    def get_cost(self): pass

    @abstractmethod
    def get_description(self): pass


class BasicInspection(CarService):
    def get_cost(self):
        return 25

    def get_description(self):
        return 'Basic Inspection'


class OilChange(CarService):
    def __init__(self, car_service: CarService):
        self.car_service = car_service

    def get_cost(self):
        return 29 + self.car_service.get_cost()

    def get_description(self):
        return self.car_service.get_description() + ' and Oil Change'


class TireRotation(CarService):
    def __init__(self, car_service: CarService):
        self.car_service = car_service

    def get_cost(self):
        return 10 + self.car_service.get_cost()

    def get_description(self):
        return self.car_service.get_description() + ' and Tire Rotation'


def main():
    service = BasicInspection()
    print('{}: {}'.format(service.get_description(), service.get_cost()))

    service = OilChange(BasicInspection())
    print('{}: {}'.format(service.get_description(), service.get_cost()))

    service = TireRotation(BasicInspection())
    print('{}: {}'.format(service.get_description(), service.get_cost()))

    service = TireRotation(OilChange(BasicInspection()))
    print('{}: {}'.format(service.get_description(), service.get_cost()))


if __name__ == '__main__':
    """
    A decorator allows us to dynamically extend the behavior of a particular object at runtime,
    without needing to resort to unnecessary inheritance.
    """
    main()
