"""
Write a Python program to read a file line by line and store it into a list.
"""

my_file = r"C:\\Users\\mipc\\Downloads\\test.txt"

with open(my_file, 'r') as file:
  mylist = file.readlines()
  
print(mylist)