"""
Write a Python program to get the size of an object in bytes.
"""

import sys

a = "112"
b = 112
c = "loopbaancoach"

def print_size(myvar):
  size = str(sys.getsizeof(myvar))
  return f"Object {myvar} size is {size} bytes."

print(print_size(a))
print(print_size(b))
print(print_size(c))