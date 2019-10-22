#!/usr/bin/python3
"""Unittest rectangle"""

import sys
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test for Rectangle class."""

    #-----task2

    def setUp(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """Test if rectangle is an instance of base"""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Base)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_valid_id(self):
        """Test Rectangle class: check for id."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r3.id, -5)

    def test_arguments(self):
        """Test with diferents numbers of arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(5, 10 , 15)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 11, 12, 13)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 13)

        r = Rectangle(5, 10, 15, 20, 25)
        self.assertEqual(r.id, 25)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 20)

    def test__private_attributes(self):
        """Test for private attributes."""
        r = Rectangle(5, 10, 15, 20, 25)
        dic = {"_Rectangle__width": 5, "_Rectangle__height": 10,
             "_Rectangle__x": 15, "_Rectangle__y": 20, "id": 25}
        self.assertEqual(r.__dict__, dic)

    #-----task3

    def test_string_arg(self):
        """Testing strings in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle("5.5", 10, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, "10.3", 10, 15, 20 )
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, "15.2")
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, "20.0")
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, 20, 25, 30)
            self.assertEqual(str(e.exception)," __init__() takes from 3 to \
                             6 positional arguments but 7 were given")

    def test_float(self):
        """Testing float values in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(5.5, 10, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10.2, 10, 15, 20 )
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15.25)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, 20.00)
        self.assertEqual("y must be an integer", str(e.exception))

    def test_zero_values(self):
        """Testing zero in every argument."""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 10, 15, 20, 25)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Rectangle(5, 0, 10, 15, 20 )
        self.assertEqual("height must be > 0",str(e.exception))

        r = Rectangle(5, 10, 0)
        self.assertEqual(r.x, 0)

        r = Rectangle(5, 10, 15, 0)
        self.assertEqual(r.y, 0)

    def test_negative(self):
        """Testing negative values in every argument."""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-5, 10, 15, 20, 25)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Rectangle(5, -10, 10, 15, 20 )
        self.assertEqual("height must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Rectangle(5, 10, -15)
        self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Rectangle(5, 10, 15, -20)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_list(self):
        """Testing list as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1, 2], 10, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, [1, 2], 10, 15, 20 )
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, [1, 2])
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, [1, 2])
        self.assertEqual("y must be an integer", str(e.exception))

    def test_tuples(self):
        """Testing tuples as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle((1, 0), 10, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, (1, 0), 10, 15, 20 )
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, (1, 0))
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, (1, 0))
        self.assertEqual("y must be an integer", str(e.exception))

    def test_dictionaries(self):
        """Testing dictionaries as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle({1: 2}, 10, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, {1: 2}, 10, 15, 20 )
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, {1: 2})
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Rectangle(5, 10, 15, {1: 2})
        self.assertEqual("y must be an integer", str(e.exception))

    #----Task4
    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r = Rectangle(5, 5, 1)
        self.assertEqual(r.area(), 25)

        r = Rectangle(100, 100, 10)
        self.assertEqual(r.area(), 10000)

        r = Rectangle(9, 1)
        r.width = 10
        r.height = 9
        self.assertEqual(r.area(), 90)

    #--task5
    
