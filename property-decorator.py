# https://www.youtube.com/watch?v=jCzT9XFZ5bw
# Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters

class Employe:
    """docstring for Employe."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last +'@gmail.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first,  self.last)

    @fullname.setter
    def fullname(self, name):
        self.first,  self.last = name.split(' ')

e1 = Employe('Ravi', 'Patel')
e1.first = 'Raj'
print('first:{}, last:{}'.format(e1.first,  e1.last))
print(e1.email)
print(e1.fullname)

e1.fullname = 'Vir Kumar'
print('first:{}, last:{}'.format(e1.first,  e1.last))
print(e1.email)
print(e1.fullname)
