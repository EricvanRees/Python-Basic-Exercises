"""
Write a Python program to move spaces to the front of a given string.
"""


def move_spaces(s):
    space_count = s.count(" ")
    start_str = " " * space_count
    return start_str + s.replace(" ", "")


print(move_spaces("this string contains spaces."))
