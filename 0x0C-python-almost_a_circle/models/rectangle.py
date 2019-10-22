#!/usr/bin/python3
""" Module comments"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @property
    def x(self):
        """getter for x attribute"""
        return self.__x

    @property
    def y(self):
        """getter for y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """setting the private width value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setting the private height value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setting the private x value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setting the private height value
        and checking for errors"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """prints the representation of the rectangle."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update a rectangle class"""

        i = 0
        if args and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                else:
                    break
                i += 1
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
