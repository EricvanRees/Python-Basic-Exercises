"""
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

"""

def calc_diff(any_int):
  if any_int > 17:
    return (any_int - 17) * 2
  else:
    return any_int - 17
  

print(calc_diff(18))
print(calc_diff(16))
