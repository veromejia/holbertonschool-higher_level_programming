#!/usr/bin/python3
"""Module comments"""


import json
import os
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inicializating objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        my_file = cls.__name__ + ".json"

        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(cls.to_dictionary(i))
        with open(my_file, 'w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_file = cls.__name__ + ".json"

        try:
            with open(my_file, 'r', encoding="UTF8") as f:
                element = cls.from_json_string(f.read())
        except:
            return []

        my_list = []

        for i in element:
            tmp = cls.create(**i)
            my_list.append(tmp)

        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV:"""
        my_file = cls.__name__ + ".csv"

        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(cls.to_dictionary(i))
        with open(my_file, 'w') as f:
            f.write(cls.to_json_string(my_list))

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        my_file = cls.__name__ + ".csv"

        try:
            with open(my_file, 'r', encoding="UTF8") as f:
                element = cls.from_json_string(f.read())
        except:
            return []

        my_list = []

        for i in element:
            tmp = cls.create(**i)
            my_list.append(tmp)

        return my_list
