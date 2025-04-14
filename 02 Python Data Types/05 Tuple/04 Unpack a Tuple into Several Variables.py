"""
Write a Python program to unpack a tuple into several variables.
"""

def unpack_tuple(mytuple):
  (a, *b) = mytuple
  return a, b

print(unpack_tuple((1, 2, 3)))