"""
Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
"""


def swap(c):
    mytable = str.maketrans('.', ',')
    return c.translate(mytable)


print(swap("32.054,23"))
