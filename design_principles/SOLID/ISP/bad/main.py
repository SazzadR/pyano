from abc import ABCMeta, abstractmethod


class WorkerInterface(metaclass=ABCMeta):
    @abstractmethod
    def work(self): pass

    @abstractmethod
    def sleep(self): pass


class HumanWorker(WorkerInterface):
    def work(self):
        print('human working...')

    def sleep(self):
        print('human sleeping...')


class AndroidWorker(WorkerInterface):
    def work(self):
        print('android working...')

    def sleep(self):
        """
        Here we forced `sleep` method which is unnecessary in the context of `AndroidWorker`,
        and thus it violate the Interface Segregation principle
        """
        pass


class Captain:
    def manage(self, worker: WorkerInterface):
        worker.work()
        worker.sleep()


def main():
    captain = Captain()
    human_worker = HumanWorker()
    android_worker = AndroidWorker()

    captain.manage(human_worker)
    captain.manage(android_worker)


if __name__ == '__main__':
    main()
