"""
Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
"""

import itertools

d= ""
vowels ='aeioI'

permutations = [d.join(e) for e in itertools.permutations(vowels)]
print(permutations)