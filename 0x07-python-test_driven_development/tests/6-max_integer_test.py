#!/usr/bin/python3
"""Unittest for max_integer([..]) module"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer function."""

    def test_valid_entry(self):
        """test with valid data """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_list(self):
        """Test with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_float(self):
        """Test with a list including floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_equal_values(self):
        """Test with equal values"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_string(self):
        """Test including an string"""
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])

if __name__ == '__main__':
    unittest.main()
