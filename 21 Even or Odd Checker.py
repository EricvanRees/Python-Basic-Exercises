"""
Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""

def even_or_odd(a_num):
  if a_num % 2 == 0:
    return "num is even"
  else:
    return "num is odd"
  
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(4))
print(even_or_odd(5))