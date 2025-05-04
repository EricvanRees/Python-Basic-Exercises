"""
Write a Python program to make combinations of 3 digits.
"""

import itertools

res = list(itertools.permutations([1,2,3]))
print(res)