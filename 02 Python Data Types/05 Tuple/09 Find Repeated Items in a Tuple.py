"""
Write a Python program to find repeated items in a tuple.
"""

from collections import Counter

def find_repeated(atuple):
  return Counter(atuple)

print(find_repeated((1,2,3,4,4,4,4,4)))