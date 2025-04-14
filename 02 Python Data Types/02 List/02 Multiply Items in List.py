"""
Write a Python program to multiply all the items in a list.
"""
from operator import mul
from functools import reduce

def multiply_list(anylist):
  res  = reduce(mul, anylist)
  print(res)

multiply_list([1,2,3,4])