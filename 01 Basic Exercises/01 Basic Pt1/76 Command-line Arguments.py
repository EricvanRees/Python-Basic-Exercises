"""
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
"""

import os

def print_args(*args):
  return os.path.basename(__file__), len(args), args

print(print_args(1, 3))