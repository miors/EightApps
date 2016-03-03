#!/usr/bin/python

import random

while True:
    user_input = input("Enter a number between 0 and 10: ")
    magic_number = int(11 * random.random())
    print("magic number is {}".format(magic_number))
    if int(user_input) == magic_number:
        print("You have won")
        break
    else:
        print("Please pick another number")