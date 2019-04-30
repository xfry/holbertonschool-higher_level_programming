#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print("{:02.0f}{:s} ".format(n, ','), end='')
    else:
        print("{:d}{:s}".format(n, (', ' if n != 99 else '\n')), end='')
