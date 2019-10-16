#!/usr/bin/python3
class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """ public instance method, that prints a list in ascending sort"""
        print(sorted(self))
