#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)
    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return (max)


if __name__ == "__main__":
    my_list = [-1, -2, -3, -4]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
