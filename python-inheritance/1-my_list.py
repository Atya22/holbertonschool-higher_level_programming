#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """custom action"""
    def print_sorted(self):
        """sorting"""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)

