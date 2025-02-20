import sys
import unittest

from exercises.calculate_factorial import factorial_recursive, process_input

class MyTestCase(unittest.TestCase):
    def test_process_input_negative_value(self):
        value, error_message = process_input("-7")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Error: Number cannot be negative")

    def test_zero_factorial(self):
        self.assertEqual(1, factorial_recursive(0))

    def test_one_factorial(self):
        self.assertEqual(1, factorial_recursive(1))

    def test_fractional_number(self):
        value, error_message = process_input("3.2")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Error: Input must be a non-negative integer")

    def test_positive_factorial(self):
        self.assertEqual(5040, factorial_recursive(7))

    def test_large_factorial(self):
        self.assertEqual(39916800, factorial_recursive(11))

    def test_before_recursion_limit(self):
        sys.setrecursionlimit(50)
        try:
            factorial_recursive(20)  # Should complete without error
        except RecursionError:
            self.fail("RecursionError raised before reaching the limit")

    def test_after_recursion_limit(self):
        sys.setrecursionlimit(1050)
        with self.assertRaises(RecursionError):
            factorial_recursive(1051)  # Should exceed limit

if __name__ == '__main__':
    unittest.main()