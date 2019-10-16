#!/usr/bin/python3
class MyInt(int):
    """Class inheriting from int."""

    def __eq__(self, other):
        """return oposite"""
        return int(self) != int(other)

    def __ne__(self, other):
        """return oposite"""
        return int(self) == int(other)
