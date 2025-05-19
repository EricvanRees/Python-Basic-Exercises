"""
Write a Python program to print all permutations with a given repetition number of characters of a given string.
"""

from itertools import permutations


def find_permutations(astr):
    return [''.join(p) for p in permutations(astr)]


print(find_permutations("321"))
