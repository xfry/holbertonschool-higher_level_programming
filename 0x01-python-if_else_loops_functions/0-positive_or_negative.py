#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{:d} negative".format(number))
elif number > 0:
    print("{:d} positive".format(number))
else:
    print("{:d} zero".format(number))
