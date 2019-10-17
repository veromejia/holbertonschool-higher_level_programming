#!/usr/bin/python3
"""Module of class Student that defines a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Inicializating objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method the retrieves a dictionary representation
        of a student instance"""
        return self.__dict__
