import math
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

    def test_factorial_recursion_limit(self):
        #get python's recursion depth limit
        large_number = sys.getrecursionlimit() // 2 #divide by 2 so that the recursive_factorial function does not hit the limit and cause error
        result_recursive = factorial_recursive(large_number)
        result_iterative = factorial_iterative(large_number)
        self.assertEqual(result_recursive, result_iterative)
        
    def test_factorial_above_recursion_limit(self):
        large_number = sys.getrecursionlimit() // 2 + 1
        # Compare against built in math factorial function
        self.assertEqual(factorial_iterative(large_number), math.factorial(large_number))

    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(10), math.factorial(10))
        self.assertEqual(factorial_iterative(0), 1)

if __name__ == '__main__':
    unittest.main()
