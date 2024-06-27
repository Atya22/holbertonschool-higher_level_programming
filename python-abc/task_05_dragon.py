#!/usr/bin/python3
""" Defines a Dragon class. """


class SwimMixin:
    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """_summary_"""
        print("The dragon roars!")
