#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    if len(my_list) < 1:
        return (None)
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return (max)


if __name__ == "__main__":
    my_list = []
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
