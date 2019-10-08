#!/usr/bin/python3
""" This module define a Rectangle class"""


class Rectangle:
    """defining the Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing objects"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the representation of the rectangle."""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
