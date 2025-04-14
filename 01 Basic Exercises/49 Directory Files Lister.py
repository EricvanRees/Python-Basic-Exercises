"""
Write a Python program to list all files in a directory.
"""

import os

path = os.getcwd()

files = [f for f in os.listdir(path) if os.path.isfile(f)]
for f in files:
  print(f)