"""
Write a Python program to check if a set is a subset of another set.
"""

def check_if_subset(aset, subset):
  z = subset.issubset(aset)
  return z
  
print(check_if_subset({1,2, 3,4}, {3,4,5}))
print(check_if_subset({1,2, 3,4}, {3,4}))