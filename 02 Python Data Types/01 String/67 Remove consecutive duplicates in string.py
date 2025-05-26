"""
Write a Python program to remove all consecutive duplicates of a given string.
"""


def remove_consecutive_duplicates(astr):
    return ''.join(set(astr))


print(remove_consecutive_duplicates("aabbccddeeff"))
