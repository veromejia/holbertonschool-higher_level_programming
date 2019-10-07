#!/usr/bin/python3
""" This module define a Rectangle class"""


class Rectangle:
    """defining the Rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the private width value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the private height value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
