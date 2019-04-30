#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print("{:02.0f}".format(n))
    else:
        print("{:d}".format(n))
