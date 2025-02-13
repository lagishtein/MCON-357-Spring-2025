import unittest
from exercises.calculate_factorial import *


class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertTrue(check_valid_input(0))

    def test_factorial_one(self):
            self.assertEqual(factorial_recursive(1), 1)
            self.assertTrue(check_valid_input(1))

    def test_factorial_negative(self):
            self.assertFalse(check_valid_input(-3))

    def test_factorial_fraction(self):
            self.assertFalse(check_valid_input('3.4'))

    def test_factorial_positive_integer(self):
        self.assertEqual(factorial_recursive(3), 6)
        self.assertTrue(check_valid_input(3))

    def test_factorial_large_number(self):
            self.assertEqual(factorial_recursive(12), 479001600)
            self.assertTrue(check_valid_input(12))

if __name__ == '__main__':
    unittest.main()
