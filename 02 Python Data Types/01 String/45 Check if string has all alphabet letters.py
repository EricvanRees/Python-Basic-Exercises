"""
Write a Python program to check whether a string contains all letters of the alphabet.
"""

import string

alphabet = set(string.ascii_lowercase)


def ispangram(input_string):
    return set(input_string.lower()) >= alphabet


print(ispangram("abcdefghijklmnopqrstuvwxyz"))
print(ispangram("abc"))
