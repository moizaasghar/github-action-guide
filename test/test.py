# test the calculator class
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 0), "Division by zero error")

if __name__ == '__main__':
    unittest.main()