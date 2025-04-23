"""
Write a Python program to check if a given number is even or odd using boolean variables.
"""

def even_or_odd(any_int):
  if any_int % 2 == 0:
    return True
  else:
    return False
  
print(even_or_odd(0))
print(even_or_odd(44))
print(even_or_odd(33))
print(even_or_odd(12))