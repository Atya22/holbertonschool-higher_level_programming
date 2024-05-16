#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
n = str(number)
last_index = len(n) - 1
last_number = int(n[last_index])
if last_number > 5: print(f"Last digit of {n} is {last_number} and is greater than 5")
elif last_number == 0: print(f"Last digit of {n} is {last_number} and is 0")
else : print(f"Last digit of {n} is and is {last_number} less than 6 and not 0")
