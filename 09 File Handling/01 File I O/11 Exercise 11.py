"""
Write a Python program to get the file size of a plain file.
"""

import os

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

def get_file_size(my_file):
  file_stats = os.stat(file_name)
  print(f'File Size in Bytes is {file_stats.st_size}')
  

get_file_size(file_name)
  