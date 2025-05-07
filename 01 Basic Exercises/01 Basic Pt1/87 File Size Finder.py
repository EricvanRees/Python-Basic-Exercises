"""
Write a Python program to get the size of a file.
"""

import os

def get_file_size(path):
  file_stats = os.stat(path)
  print(f"File size in Bytes is {file_stats.st_size}")
  
path = r"C:\\Users\\mipc\\Downloads\\test.txt"
get_file_size(path)