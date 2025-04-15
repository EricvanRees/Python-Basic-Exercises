"""
Write a Python function to check whether a number falls within a given range.
"""

def check_in_range(anum, min, max):
  if min <= anum <= max:
    return True
  else:
    return False
  
print(check_in_range(8, 0, 10))
print(check_in_range(8, 0, 7))
print(check_in_range(8, 0, 8))