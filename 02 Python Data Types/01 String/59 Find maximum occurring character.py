"""
Write a Python program to find the maximum number of characters in a given string.
"""
from collections import Counter


def max_occurring_char(astr):
    return Counter(astr).most_common(1)


print(max_occurring_char("Welcome to w3resource"))
