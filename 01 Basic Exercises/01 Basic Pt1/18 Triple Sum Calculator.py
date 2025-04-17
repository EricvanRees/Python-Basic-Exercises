"""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

"""

def calc_sum(a, b, c):
  if a == b == c:
    return (a + b + c) * 2
  else:
    return a + b + c
  

print(calc_sum(1, 1, 1))
print(calc_sum(4, 5, 6))
print(calc_sum(6, 7, 8))
