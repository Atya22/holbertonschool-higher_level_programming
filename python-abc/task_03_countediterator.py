#!/usr/bin/env python3
"""Defines a CountedIterator class. """


class CountedIterator:
    def __init__(self, iterable):
        """Initialize the CountedIterator object."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Return the next item from the iterator. """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")

    def get_count(self):
        """Return the number of items returned by the iterator."""
        return self.counter
