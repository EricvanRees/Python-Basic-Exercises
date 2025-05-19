"""
Write a Python program to find the first non-repeating character in a given string.
"""


def find_non_repeating_char(astr):
    last_char = astr[0]
    for letter in astr:
        if last_char == letter:
            continue
        else:
            print(letter)
            break


find_non_repeating_char("aaaabaaaaa")
