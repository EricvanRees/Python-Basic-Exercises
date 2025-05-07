"""
Write a Python program to create an intersection of sets.
"""

set1 = {1,2,3,4}
set2 = {3,4,5,6}

def set_intersect(a, b):
  return a & b

print(set_intersect(set1, set2))