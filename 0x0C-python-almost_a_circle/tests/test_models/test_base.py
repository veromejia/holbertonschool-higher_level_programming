#!/usr/bin/python3
"""Unittest for base class"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    """ test for class base and its methods"""

    def setUp(self):
        """Imports module"""
        Base._Base__nb_objects = 0
        pass

    def test_empty_id(self):
        """test with no id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_valid_id(self):
        """test with a valid int id"""
        b = Base(25)
        self.assertEqual(b.id, 25)

    def test__float_id(self):
        """test for float input."""
        b = Base(1.5)
        self.assertEqual(b.id, 1.5)

    def test_zero(self):
        """test with id zero"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_id(self):
        """test with negative id"""
        b = Base(-25)
        self.assertEqual(b.id, -25)

    def test_string_id(self):
        """testing with a string argument"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_list(self):
        """testing with a list argument"""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_tuple_id(self):
        """test with a tuple argument"""
        b = Base((5, 7))
        self.assertEqual(b.id, (5, 7))

    def test_dict_id(self):
        """test base id, with dict argument"""
        b = Base({12: 13})
        self.assertEqual(b.id, {12: 13})

    def test_type(self):
        """test for type."""
        b = Base()
        self.assertEqual(type(b), Base)

    def test_instance(self):
        """ test for instance"""
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_number_arguments(self):
        """test if arg count is greater than 1"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_private_id(self):
        """Test if nb_objectse is private"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    # -----task 15
    def test_json_none(self):
        """test for none in to_json_string."""
        js = Base.to_json_string(None)
        self.assertEqual(js, "[]")

    def test_json_empty(self):
        """test for empty json"""
        sq = Base.to_json_string([])
        self.assertEqual(sq, "[]")

    def test_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_json_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 2)

    def test_json_type(self):
        """ test the type in to_json_string"""
        to_js = Square(1)
        json_dict = to_js.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_json_float(self):
        """Test for float in to_json_string."""
        rec = Base.to_json_string(5.5)
        self.assertEqual(type(rec), str)

    def test_json_rectangle(self):
        rec = Rectangle(5, 7, 2, 8)
        json_dict = Base.to_json_string([rec.to_dictionary()])
        self.assertEqual(type(json_dict), str)

    def test_json_dictionaries(self):
        """testing json string widh dictionaries"""
        dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_d, str))

    def test_json_more_dicts(self):
        """Test for multiple dicts in to_json_string."""
        dics = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(type(dics), str)

    def test_json_empty_dict(self):
        """Test for empty dict in to_json_string."""
        dic = Base.to_json_string([{}])
        self.assertEqual(dic, "[{}]")

    def test_save_None_file(self):
        """Test for None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_empty_file(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_valid_file(self):
        """Test class method save_to_file with normal types."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Rectangle.json")

    def test_save_valid_file(self):
        """Test class method save_to_file with normal types."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        res = ('[{"id": 5, "size": 5, "x": 0, "y": 0},' +
               ' {"id": 6, "size": 7, "x": 9, "y": 1}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")

    # -----task 18
    def dictionary(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    # -----task19
    def test_load_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertNotEqual(id(li[0]), id(lo[0]))
        self.assertEqual(str(li[0]), str(lo[0]))
        self.assertNotEqual(id(li[1]), id(lo[1]))
        self.assertEqual(str(li[1]), str(lo[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        li = [s1, s2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertNotEqual(id(li[0]), id(lo[0]))
        self.assertEqual(str(li[0]), str(lo[0]))
        self.assertNotEqual(id(li[1]), id(lo[1]))
        self.assertEqual(str(li[1]), str(lo[1]))


if __name__ == "__main__":
    unittest.main()
