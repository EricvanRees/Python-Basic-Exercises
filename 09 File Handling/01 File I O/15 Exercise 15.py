"""
Write a Python program to read a random line from a file.
"""

import random

my_file = r"C:\\Users\\mipc\\Downloads\\test.txt"

with open(my_file, 'r') as file:
  line_count = len(file.readlines())
  random_line_nr = random.randint(0, line_count)
  
with open(my_file, 'r') as file:
  print(file.readlines()[random_line_nr])
  