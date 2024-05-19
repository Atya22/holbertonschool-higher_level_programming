#!/usr/bin/python3
from sys import argv

print(dir())

def func():
    argc = len(argv)
    sum = 0

    for i in range(1, argc):
        sum += int(argv[i])

    print(sum)


print(dir())

if __name__ != "__main__":
    func()
