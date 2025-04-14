"""
Write a Python program to remove item(s) from a given set.
"""

def remove_from_set(myset, *args):
  for arg in args:
    myset.remove(arg)
    
  return myset

print(remove_from_set({1,2,3,4,5}, 4, 5))