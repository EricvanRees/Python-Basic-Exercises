"""
Write a Python program to triple all numbers in a given list of integers. Use Python map.
"""

def triple(x):
  return x * 3

y = map(triple, [1,2,3,4])
print(list(y))