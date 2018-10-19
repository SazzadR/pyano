class Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = '{}.{}@example.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __str__(self) -> str:
        return '{} - {}'.format(self.full_name(), self.email)

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __len__(self):
        return len(self.full_name())


employee_1 = Employee('Corey', 'Schafer', 50000)
print(repr(employee_1))
print(len(employee_1))
