"""
Write a Python program to read a file line by line store it into a variable.
"""

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

with open(file_name) as file:
  all_lines = file.readlines()
  
print(all_lines)