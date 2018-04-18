#!/usr/bin/python3

import unittest
from calculator import cal

class TestCalculator(unittest.TestCase):
    '''Testing the calculator'''

    def setUp(self):
        '''Set up testing objects'''
        self.a = 439
        self.b = 4

    def test_add(self):
        '''Testing add menthod'''
        calculator = cal(self.a, self.b)
        # print(calculator.add())

        self.assertEqual(calculator.add(),443)

    def test_subtract(self):
        '''Testing subtract method'''
        calculator = cal(self.a, self.b)
        self.assertEqual(calculator.sub(), 435)


if __name__ == '__main__':
    unittest.main(verbosity=2)
