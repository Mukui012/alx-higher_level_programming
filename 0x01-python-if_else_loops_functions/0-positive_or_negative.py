#!/usr/bin/python3
import random
number = random.randint(-10, 10)
num = int(input("Please enter an integer: "))
if num < 0:
    print(num, "is negative")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is positive")
