"""
Write a Python program to get the frequency of elements in a list.
"""

from collections import Counter

def get_freq(alist):
  return Counter(alist)

print(get_freq(['a', 'b', 'b', 'c', 'c', 'c']))