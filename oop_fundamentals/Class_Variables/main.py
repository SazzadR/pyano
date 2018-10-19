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
        return '{} {}'.format(self.first_name, self.last_name)

    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self) -> int:
        return int(self.salary * self.raise_amount)


emp_1 = Employee('Cory', 'Schafer', 5000)
emp_2 = Employee('John', 'Doe', 2000)

print('Number of Employees: {}'.format(Employee.num_of_employees))

print('######### Increase Employee_1\'s raise #########')

print('Class variable: {}'.format(Employee.raise_amount))
print('Employee_1 raise: {}'.format(emp_1.raise_amount))
print('Employee_2 raise: {}'.format(emp_2.raise_amount))

print('######### Increase Employee_1\'s raise #########')

emp_1.raise_amount = 1.05
print('Class variable: {}'.format(Employee.raise_amount))
print('Employee_1 raise: {}'.format(emp_1.raise_amount))
print('Employee_2 raise: {}'.format(emp_2.raise_amount))

print('######### Increase all Employee\'s raise #########')

Employee.raise_amount = 1.05
print('Class variable: {}'.format(Employee.raise_amount))
print('Employee_1 raise: {}'.format(emp_1.raise_amount))
print('Employee_2 raise: {}'.format(emp_2.raise_amount))

