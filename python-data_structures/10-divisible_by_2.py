#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_result = []
    for i in range(len(my_list)):
        res = False
    if my_list[i] % 2 == 0:
        res = True
    else:
        res = False
    list_result.append(res)
    return list_result
