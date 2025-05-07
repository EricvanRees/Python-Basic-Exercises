"""
Write a Python program to create set difference.
"""

set1 = {1,2,3,4}
set2 = {3,4,5,6}

def set_diff(a, b):
  return a.difference(b)

print(set_diff(set1, set2))