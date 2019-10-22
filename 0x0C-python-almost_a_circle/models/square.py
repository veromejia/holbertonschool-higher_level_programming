#!/usr/bin/python3
""" Module for Square class"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inicializating objects"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints the representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        """getter for size attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """setting the size  value and checking for errors"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update square"""
        i = 0
        if args and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
