"""
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sum_ints(int1, int2):
  sums = int1 + int2
  if sums >= 15 and sums <= 20:
    return 20
  else:
    return sums
  

print(sum_ints(10, 19))
print(sum_ints(5, 19))
print(sum_ints(10, 8))