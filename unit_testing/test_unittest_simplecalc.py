import pytest

import pyodbc

# pytest and unittest are 2 diff packages to allow us to run tests in python

from simple_calc import SimpleCalc

import unittest


class CalcTests(unittest.TestCase):  # inheriting from unittest so all code can be used

    calc = SimpleCalc()  # making and instance of the calculator, as that is what will be tested

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)  # an assertion from the TestCase class

    # using assert equal, pass in the function + the arguments(examples), then the expected output

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

# should not just be running the file, should run tests in the terminal
#   how to do this is in theory.txt


