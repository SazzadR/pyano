from abc import ABCMeta, abstractmethod


class EmployeeInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employee_id, employee_name): pass

    @abstractmethod
    def get_minimum_salary(self): pass


class EmployeeBonusInterface(metaclass=ABCMeta):
    @abstractmethod
    def calculate_bonus(self, salary): pass


class Employee(EmployeeInterface, EmployeeBonusInterface):
    def __init__(self, employee_id, employee_name):
        super().__init__(employee_id, employee_name)
        self.employee_id = employee_id
        self.employee_name = employee_name

    def __str__(self):
        return 'ID: {}, Name {}'.format(self.employee_id, self.employee_name)

    def calculate_bonus(self, salary):
        pass

    def get_minimum_salary(self):
        pass


class PermanentEmployee(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.1

    def get_minimum_salary(self):
        return 100000


class TemporaryEmployee(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.05

    def get_minimum_salary(self):
        return 50000


class ContractEmployee(EmployeeInterface):
    def __init__(self, employee_id, employee_name):
        super().__init__(employee_id, employee_name)
        self.employee_id = employee_id
        self.employee_name = employee_name

    def get_minimum_salary(self):
        return 25000


def main():
    permanent_emp_1 = PermanentEmployee(1, 'John')
    temporary_emp_1 = TemporaryEmployee(2, 'Jason')
    contract_emp_1 = ContractEmployee(3, 'Mike')

    print('Employee {}, Bonus: {}'.format(permanent_emp_1, permanent_emp_1.calculate_bonus(100000)))
    print('Employee {}, Bonus: {}'.format(temporary_emp_1, temporary_emp_1.calculate_bonus(50000)))
    # There is no `calculate_bonus()` method in `contract_emp_1` object
    # print('Employee {}, Bonus: {}'.format(contract_emp_1, contract_emp_1.calculate_bonus(25000)))


if __name__ == '__main__':
    main()
