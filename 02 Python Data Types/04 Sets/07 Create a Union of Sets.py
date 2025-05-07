"""
Write a Python program to create a union of sets.
"""

set1 = {1,2,3,4}
set2 = {3,4,5,6}

def set_union(a, b):
  return a.union(b)

print(set_union(set1, set2))