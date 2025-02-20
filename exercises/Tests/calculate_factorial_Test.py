import unittest
import sys
from calculate_factorial import process_input, factorial_recursive


class test_factorial(unittest.TestCase):
    # test that it returns 1 for 0
    def test_factorial_zero(self):
        self.assertEqual(factorial_recursive(0),1)

    #tests that it returns 1 for 1
    def test_factorial_one(self):
        self.assertEqual(factorial_recursive(1),1)

    #tests for negative number
    def test_negative_input_returns_message(self):
        value, error = process_input(-7)
        self.assertIsNone(value) #doesnt return value because doesnt work with neagtives
        self.assertEqual(error, "Number must be positive!")

    #test that fraction doesnt work
    def test_fraction_returns_message(self):
        value, error = process_input(1.8)
        self.assertIsNone(value) #doesnt return value because doesnt work with fractions
        self.assertEqual(error, "Number must be an integer!")

    #tests for positive input
    def test_positive_number(self):
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(3), 6)

    #test for number greater than 10
    def test_large_number(self):
        self.assertEqual(factorial_recursive(11), 39916800)

    #recursion limit- right before limit
    def test_recursion_before_limit(self):
        limit = sys.getrecursionlimit()
        value, error = process_input(limit-1)
        self.assertIsNotNone(value)
        self.assertIsNone(error)

    #test recursion after limit
    def test_recursion_after_limit(self):
        limit = sys.getrecursionlimit()
        value, error =process_input(limit+3)
        self.assertIsNone(value)
        self.assertEqual(error,"Number exceeded the recursion limit!")

if __name__ == '__main__':
    unittest.main()
