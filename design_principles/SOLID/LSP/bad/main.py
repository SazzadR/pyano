from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name

    def __str__(self):
        return 'ID: {}, Name {}'.format(self.employee_id, self.employee_name)

    @abstractmethod
    def calculate_bonus(self, salary): pass


class PermanentEmployee(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.1


class TemporaryEmployee(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.05


class ContractEmployee(Employee):
    def calculate_bonus(self, salary):
        raise NotImplemented('Contract employees are not eligible for a bonus.')


def main():
    permanent_emp_1 = PermanentEmployee(1, 'John')
    temporary_emp_1 = TemporaryEmployee(2, 'Jason')
    # contract_emp_1 = ContractEmployee(3, 'Mike')

    print('Employee {}, Bonus: {}'.format(permanent_emp_1, permanent_emp_1.calculate_bonus(100000)))
    print('Employee {}, Bonus: {}'.format(temporary_emp_1, temporary_emp_1.calculate_bonus(50000)))
    # print('Employee {}, Bonus: {}'.format(contract_emp_1, contract_emp_1.calculate_bonus(25000)))


if __name__ == '__main__':
    main()
