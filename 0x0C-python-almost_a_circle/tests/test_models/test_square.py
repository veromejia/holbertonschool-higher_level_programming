#!/usr/bin/python3
""" Unittest for square class """


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test for Square class"""

    def setUp(Self):
        Base._Base__nb_objects = 0

    # -----task10-11
    def test_isinstance(self):
        """Test if Square is instance of rectangle"""
        s1 = Square(4)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Rectangle)

        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_valid_id(self):
        """Test square class: check for id."""
        s1 = Square(2)
        self.assertEqual(s1.id, 1)

        s2 = Square(10, 2, 12, 0)
        self.assertEqual(s2.id, 0)

        s3 = Square(10, 2, 4, -5)
        self.assertEqual(s3.id, -5)

    def test_attributes(self):
        """testing every argument"""
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 5)

    def test_arguments(self):
        """Test with diferents numbers of arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError) as e:
            Rectangle(1)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

        with self.assertRaises(TypeError) as e:
            s = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

        s = Square(10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(5, 10, 15)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 15)

        s = Square(5, 10, 15, 20)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 15)

    def test_string_arg(self):
        """Testing strings in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Square("5.5", 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, "15.2")
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, "20.0")
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, 15, 20, 25)
            self.assertEqual(str(e.exception), " __init__() takes from 2 to \
                             5 positional arguments but 6 were given")

    def test_float(self):
        """Testing strings in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Square(5.5, 15, 20, 25)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 15.2)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, 20.0)
        self.assertEqual("y must be an integer", str(e.exception))

    def test_Zero_values(self):
        """Testing Zero in every argument."""
        with self.assertRaises(ValueError) as e:
            r = Square(0, 15, 20, 25)
        self.assertEqual("width must be > 0", str(e.exception))

        r = Square(5, 0)
        self.assertEqual(r.y, 0)

        r = Square(5, 10, 0)
        self.assertEqual(r.y, 0)

    def test_negative(self):
        """Testing negative values in every argument."""
        with self.assertRaises(ValueError) as e:
            r = Square(-5, 10, 15, 20,)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Square(5, -15)
        self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r = Square(5, 10, -20)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_list(self):
        """Testing list as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Square([1, 2], 10, 15, 20)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, [1, 2])
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, [1, 2])
        self.assertEqual("y must be an integer", str(e.exception))

    def test_tuples(self):
        """Testing tuples as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Square((1, 0), 10, 15, 2)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, (1, 0))
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, (1, 0))
        self.assertEqual("y must be an integer", str(e.exception))

    def test_dictionaries(self):
        """Testing dictionaries as value in every argument."""
        with self.assertRaises(TypeError) as e:
            r = Square({1: 2}, 10, 15, 2)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, {1: 2})
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r = Square(5, 10, {1: 2})
        self.assertEqual("y must be an integer", str(e.exception))

    def test_area(self):
        r = Square(3)
        self.assertEqual(r.area(), 9)

        r = Square(5, 5, 1)
        self.assertEqual(r.area(), 25)

        r = Square(100, 100, 10)
        self.assertEqual(r.area(), 10000)

        r = Square(9, 1)
        r.width = 10
        r.height = 10
        self.assertEqual(r.area(), 100)

    # -----task12
    def test_update(self):
        """testing the public method update"""
        r = Square(10, 10, 10, 10)
        r.update(1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 10")
        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Square] (89) 10/10 - 2")
        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Square] (89) 3/10 - 2")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Square] (89) 3/4 - 2")

    def test_kwargs(self):
        """testing kwargs in funcion update"""
        r = Square(10, 10, 10, 10)
        r.update(width=1)
        self.assertEqual(r.__str__(), "[Square] (10) 10/10 - 10")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Square] (10) 2/10 - 10")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Square] (89) 3/1 - 10")

    # -----task14
    def test_dictionary(self):
        """Test to_dictionary method."""
        r = Square(10, 2, 1)
        r_dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(r.to_dictionary(), r_dictionary)

        r = Square(10, 15)
        r_d = {'id': 2, 'x': 15, 'size': 10, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_d)


if __name__ == '__main__':
    unittest.main()
