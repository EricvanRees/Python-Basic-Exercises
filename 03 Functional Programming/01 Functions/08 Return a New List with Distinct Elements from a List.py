"""
Write a Python function that takes a list and returns a new list with distinct elements from the first list.

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

def return_distinct(alist):
  newset = set(alist)
  return list(newset)

print(return_distinct([1,2,3,3,3,3,4,5]))