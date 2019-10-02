#!/usr/bin/python3
class Square:
    ''' Square class'''
    def __init__(self, size=0):
        ''' inizializing fields '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        '''defining the area'''
        s_area = self.__size**2
        return s_area
