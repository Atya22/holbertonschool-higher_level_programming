#!/usr/bin/python3
def print_last_digit(number):
    s = str(number)
    last_digit = s[-1]

    if s.isnumeric():
      print("{}".format(last_digit), end="")
      
    return int(last_digit)
    