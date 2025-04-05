"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

import sys

def print_shell_mode():
  is_64bits = sys.maxsize > 2**32
  print(is_64bits)

  if is_64bits:
      print('Python is running as 64-bit application')
  else:
      print('Python is running as 32-bit application')
      
print_shell_mode()