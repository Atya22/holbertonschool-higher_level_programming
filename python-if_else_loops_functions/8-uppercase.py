#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        suffix = "\n" if i == len(str) - 1 else ""
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upp = chr(ord(str[i]) - 32)
            print("{}".format(upp), end=suffix)
        else:
            print("{}".format(str[i]), end=suffix)
