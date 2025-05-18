"""
Write a Python program to lowercase the first n characters in a string.
"""


def print_lowercase(astr, n):
    return astr[0: n].lower() + astr[n:]


print(print_lowercase("PYTHON", 2))
