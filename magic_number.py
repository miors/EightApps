#!/usr/bin/python

import random

while True:
    user_input = input("Enter a number between 0 and 10: ")
    magic_number = int(11 * random.random())
    if int(user_input) == magic_number:
        print("You guessed the correct number. You have won")
        break
    else:
        print("magic number is {}".format(magic_number))
        print("Please pick another number")