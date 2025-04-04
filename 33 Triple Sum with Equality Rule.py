"""
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

def sum_ints(a, b, c):
  if a == b == c:
    return 0
  else:
    return a + b + c


print(sum_ints(1,2,3)) 
print(sum_ints(1,1,1)) 
print(sum_ints(4,2,3)) 