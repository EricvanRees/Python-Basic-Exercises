"""
Write a Python program to read an entire text file.
"""

my_file = r"C:\\Users\\mipc\\Downloads\\test.txt"

with open(my_file, 'r') as file:
  # read all lines
  # print(file.readlines())
  
  #print each line separately and deleting line breaks:
  lines = file.readlines()
  for line in lines:
    print(line.strip())
    
# read all file content using "read" method
print("reading file contents using read method:")
with open(my_file, 'r') as file:
  print(file.read())
