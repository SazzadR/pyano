from abc import ABCMeta, abstractmethod


class ManageableInterface(metaclass=ABCMeta):
    @abstractmethod
    def be_managed(self): pass


class WorkableInterface(metaclass=ABCMeta):
    @abstractmethod
    def work(self): pass


class SleepableInterface(metaclass=ABCMeta):
    @abstractmethod
    def sleep(self): pass


class HumanWorker(WorkableInterface, SleepableInterface, ManageableInterface):
    def work(self):
        print('human working...')

    def sleep(self):
        print('human sleeping...')

    def be_managed(self):
        self.work()
        self.sleep()


class AndroidWorker(WorkableInterface, ManageableInterface):
    def work(self):
        print('android working...')

    def be_managed(self):
        self.work()


class Captain:
    def manage(self, worker: ManageableInterface):
        worker.be_managed()


def main():
    captain = Captain()
    human_worker = HumanWorker()
    android_worker = AndroidWorker()

    captain.manage(human_worker)
    captain.manage(android_worker)


if __name__ == '__main__':
    main()
