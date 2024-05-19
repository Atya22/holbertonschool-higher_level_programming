#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        print("")
    for i in range(len(str)):
        suffix = "\n" if i == len(str) - 1 else ""
        upp = ""
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upp = chr(ord(str[i]) - 32)
        else:
            upp = str[i]
        print("{}".format(upp), end=suffix)
