"""
Write a Python program to sort a given dictionary by key.
"""

def sort_dict(adict):
  return dict(sorted(adict.items()))

print(sort_dict({"z": 7, "a": 4, "f": 9}))