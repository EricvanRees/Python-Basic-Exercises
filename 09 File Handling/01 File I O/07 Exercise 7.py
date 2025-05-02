"""
Write a Python program to read a file line by line store it into an array.
"""


file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

def file_to_array(filename):
  my_array = []
  with open(filename) as file:
    my_array = file.readlines()
  
  print(my_array)
  
file_to_array(file_name)