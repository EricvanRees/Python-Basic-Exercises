"""
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""
import math

def calc_fact(anynum):
  if anynum > 0:
    return math.factorial(anynum)
  else:
    return False
  
print(calc_fact(6))