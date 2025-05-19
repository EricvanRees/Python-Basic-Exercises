"""
Write a Python program to find the first repeated character in a given string.
"""


def find_first_repeated_char(astr):
    char_count = {}

    for char in astr:
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1

    for key, value in char_count.items():
        if value == 2:
            return key


print(find_first_repeated_char("sisio"))
