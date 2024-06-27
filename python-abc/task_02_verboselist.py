#!/usr/bin/python3
"""Defines a VerboseList class. """


class VerboseList(list):

    def append(self, item):
        """Append an item to the list."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list with multiple items."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item from the list."""
        super().remove(item)
        print(f"Removed [{item}] from the list")

    def pop(self, index=-1):
        """Pop an item from the list."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
