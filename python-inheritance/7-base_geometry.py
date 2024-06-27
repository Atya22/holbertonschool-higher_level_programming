#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer greater than 0."""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
