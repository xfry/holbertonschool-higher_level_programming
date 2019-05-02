#!/usr/bin/python3
def uppercase(str):
    up_letters = range(65, 91)
    low_letters = range(97, 127)
    new_str = ""
    for character in str:
        if ord(character) > 96 and ord(character) < 127:
            new_str += chr(up_letters[low_letters.index(ord(character))])
        else:
            new_str += character
    print(new_str)
