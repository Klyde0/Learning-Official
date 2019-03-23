# Python Object-Oriented Programming
# Classes are useful to logically group data and functions (attributes/methods)
# method = function associated with a class

# Employees in a company
# Class= blueprint for creating instances (objects) of that class
# Instances (Objects) contain data/attributes unique to each instance


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return f'{self.first} {self.last}'

    def fullname_email(self):
        return f'{self.first} {self.last} at {self.email}'

emp_1 = Employee('Brian', 'Pok', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname_email())
