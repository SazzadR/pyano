import random

from core.observer import EC2Observer


class EC2Monitor(object):
    MAX_CPU_USAGE_PERCENTAGE = 80

    def __init__(self):
        self.observers = []

    def monitor(self):
        current_cpu_usage = round(self.current_cpu_usage(), 2)
        if current_cpu_usage > self.MAX_CPU_USAGE_PERCENTAGE:
            self._notify()
        else:
            print("System looks cool, current CPU usage is {}%".format(current_cpu_usage))

    def current_cpu_usage(self):
        return random.random() * 100

    def attach(self, observer: EC2Observer):
        self.observers.append(observer)

    def detach(self, observer):
        pass

    def _notify(self):
        for observer in self.observers:
            observer.handle()
