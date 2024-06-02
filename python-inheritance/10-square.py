#!/usr/bin/python3
""" Module for task 10"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size):
        """initilaze"""
        self.integer_validator("size", size)
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
