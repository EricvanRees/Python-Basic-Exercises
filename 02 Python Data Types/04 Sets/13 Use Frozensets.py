"""
Write a Python program that uses frozensets.

Note: Frozensets behave just like sets except they are immutable.
"""

def frozen_set(alist):
  return frozenset(alist)

print(frozen_set([1,2,3,4]))