#!/usr/bin/python3
from sys import argv


def func():
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    func()
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
