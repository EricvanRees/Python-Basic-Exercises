"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def eq_or_five(int1, int2):
  sums = int1 + int2
  diff = int1 - int2
  if int1 == int2:
    return True
  elif sums == 5:
    return True
  elif diff == 5:
    return True
  else:
    return False
  
print(eq_or_five(2, 2))
print(eq_or_five(2, 3))
print(eq_or_five(5, 0))
print(eq_or_five(8, 3))
