"""
Write a Python program to check whether a file exists.
"""

import os

def check_for_file(path):
  check_file = os.path.isfile(path)

  print(check_file)
  
check_for_file("./01 Formatted Twinkle Poem.py")