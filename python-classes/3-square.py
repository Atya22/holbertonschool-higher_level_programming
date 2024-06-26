#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Square class."""
    def __init__(self, size=0):
        """__init__ method for the Square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

