"""
Write a Python program to remove duplicate characters from a given string.
"""

from collections import Counter


def remove_duplicates(astr):
    letter_count = Counter(astr)
    for letter in letter_count:
        if letter_count[letter] > 1:
            index = astr.rfind(letter)
            astr = astr[:index] + astr[index + 1:]

    return astr


print(remove_duplicates("w3resource"))
