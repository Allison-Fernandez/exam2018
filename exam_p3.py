class Employee:
    """
    the base class
    """
    nextIdNum = 0
    def __init__(self, name):
        self.name = name
        self.idNum = Employee.nextIdNum
        Employee.nextIdNum += 1

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate


    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        return self.hourly_rate * hours_worked


class Exempt_Employee(Employee):
    
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary


    # Overrides the superclass method.
    def annual_pay(self, annual_pay):
        return self.annual_salary


class Manager(Exempt_Employee):
    
    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus


def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
