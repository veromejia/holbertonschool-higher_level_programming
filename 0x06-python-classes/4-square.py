#!/usr/bin/python3
class Square:
    ''' Square class'''

    def __init__(self, size=0):
        ''' inizializing fields '''
        self.size = size

    @property
    def size(self):
        '''Retrieve size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the value to the size'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        '''defining the area'''
        s_area = self.__size**2
        return s_area
