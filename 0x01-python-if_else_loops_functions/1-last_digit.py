#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number < 0:
    lastDigit = ((-1 * number) % 10) * -1
msg1 = "Last digit of {:d} is {:d} and is greater than 5"
msg3 = "Last digit of {:d} is {:d} and is less than 6 and not 0"

if lastDigit > 5:
    print(msg1.format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastDigit))
elif lastDigit < 6 & number != 0:
    print(msg3.format(number, lastDigit))
