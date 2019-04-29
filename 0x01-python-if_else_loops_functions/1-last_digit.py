#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number%10
if lastDigit > 5:
    print("last digit of {:d} is {:d} and is greather than 5".format(number, lastDigit))
elif lastDigit == 0:
    print("last digit of {:d} is {:d} and is 0".format(number, lastDigit))
elif lastDigit < 6 & number != 0:
    print("last digit of {:d} and is {:d} less than 6 and not 0".format(number, lastDigit))
