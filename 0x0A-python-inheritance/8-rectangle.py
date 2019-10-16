#!/usr/bin/python3
"""Module 8-rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry Class"""

    def __init__(self, width, height):
        """ Inicializating objects"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
