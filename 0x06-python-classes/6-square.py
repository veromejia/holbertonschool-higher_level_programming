#!/usr/bin/python3
class Square:
    ''' Square class'''

    def __init__(self, size=0, position=(0, 0)):
        ''' inizializing fields '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Retrieves the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''sets the position of the square'''
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0])is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''defining the area'''
        s_area = self.__size**2
        return s_area

    def my_print(self):
        ''' print a square'''
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
