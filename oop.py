# https://youtu.be/RSl87lqOXDE
# Python OOP Tutorial 4: Inheritance - Creating Subclasses

class Employee:

    raise_amount = 1.05
    no_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.no_of_emp += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    def raise_pay(self):
        self.pay = self.pay * self.raise_amount

    @property
    def email(self):
        return self.first + '.' + self.last + '@gmail.com'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
class Developer(Employee):
    raise_amount = 1.2

    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        self.prog_lan = prog_lan


e1 = Employee('ravi', 'Patel', 10000)
e2 = Developer('Raj', 'Kumar', 20000,'python')



# import datetime
# my_date = datetime.date(2020, 10, 26)
# print(e1.is_workday(my_date))

# e3 = Employee.from_string('raj-bhai-40000')
# print(e3.pay)

# e1.raise_pay()
# print(e1.pay)
# print(e2.pay)
#
# Employee.set_raise_amt(1.1)
#
# e1.raise_pay()
# e2.raise_pay()
# print(e1.pay)
# print(e2.pay)
# print(e2.prog_lan)
# print(Employee.__dict__)
# print(help(Employee))
#
# e2.set_raise_amt(2)
# e1.raise_pay()
# e2.raise_pay()
#
# print(e1.pay)
# print(e2.pay)
