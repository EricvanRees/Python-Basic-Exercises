"""
Write a Python program to test whether all numbers in a list are greater than a certain number.
"""

def greater_than(alist, n):
  return [i for i in alist if i > n]

print(greater_than([1,2,3,4,5,6,7,8], 4))