"""
Write a Python program to remove an item from a set if it is present in the set.
"""

def remove_from_set(myset, *args):
  for arg in args:
    if arg in myset:
      myset.remove(arg)
    else:
      return False
    
  return myset

print(remove_from_set({1,2,3,4,5}, 4, 5))