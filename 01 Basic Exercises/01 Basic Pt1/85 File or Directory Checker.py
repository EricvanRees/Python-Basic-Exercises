"""
Write a Python program to check whether a file path is a file or a directory.
"""
import os

def check_path(path):
  if os.path.isdir(path):
    print("path is a dir")
  elif os.path.isfile(path):
    print("path is a file")
  else:
    return False
  
path = r"C:\\Users\\mipc\\Downloads\\test.txt"
dir_path = r"C:\\Users\\mipc\\Downloads"

check_path(path)
check_path(dir_path)