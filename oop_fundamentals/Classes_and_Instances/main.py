class Employee:
    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@company.com'.format(self.first_name.lower(), self.last_name.lower())

    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('Cory', 'Schafer', 5000)
emp_2 = Employee('John', 'Doe', 2000)

print(emp_1)
print(emp_2.full_name())
