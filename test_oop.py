import unittest
from oop import Employee
import math
print(unittest.__file__)

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Ravi','Patel',10_000)
        self.emp_2 = Employee('Raj','Kumar',20_000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Ravi.Patel@gmail.com')
        self.assertEqual(self.emp_2.email, 'Raj.Kumar@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Ravi Patel')
        self.assertEqual(self.emp_2.fullname, 'Raj Kumar')


if __name__ == '__main__':
    unittest.main()
