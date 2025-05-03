"""
Write a Python program to print a list of space-separated elements.
"""

def add_spaces(alist):
  newlist = [f' {item} ' for item in alist]
  return newlist

print(add_spaces([1,2,3,4]))