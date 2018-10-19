class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@company.com'.format(self.first_name.lower(), self.last_name.lower())

        Employee.num_of_employees += 1

    def __str__(self) -> str:
        return self.full_name()

    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, developers=None):
        super().__init__(first_name, last_name, salary)
        if developers is None:
            self.developers = []
        else:
            self.developers = developers

    def print_developers(self):
        for developer in self.developers:
            print('--->', developer.full_name())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, primary_language):
        super().__init__(first_name, last_name, salary)
        self.primary_language = primary_language


# developer_1 = Developer('Cory', 'Schafer', 5000, 'Python')
# print(developer_1.salary)
# developer_1.apply_raise()
# print(developer_1.salary)

developer_1 = Developer('Cory', 'Schafer', 5000, 'Python')
developer_2 = Developer('Mark', 'Twain', 12000, 'C++')

manager_1 = Manager('Peter', 'Parker', 50000, [developer_1, developer_2])
print(manager_1.print_developers())
