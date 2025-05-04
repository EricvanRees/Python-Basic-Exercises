"""
Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.
"""

import itertools

mystr = ''

res = [mystr.join(e) for e in itertools.permutations("1234")]
print(res)