"""
Write a Python program to add member(s) to a set.
"""

def add_to_set(myset, *args):
  for arg in args:
    myset.add(arg)
  
  return myset


print(add_to_set({"a", "b", "c"}, 1))