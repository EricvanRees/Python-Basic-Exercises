"""
Write a Python program to count the number of lines in a text file.
"""

def count_lines(my_file):
  count = 0
  with open(my_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      count+=1
      
  print(f"file has {count} line(s)")

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"
count_lines(file_name)