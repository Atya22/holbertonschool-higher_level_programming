#!/usr/bin/python3

def divisible_by_2(my_list=[]):
  list_result = []
  for i in range(len(my_list)):
    res = False
    if my_list[i] % 2 == 0 and my_list[i] > 0:
        res = True
    else:
        res = False
    list_result.append(res)
  return list_result

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1