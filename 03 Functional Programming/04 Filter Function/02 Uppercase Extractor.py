"""
Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings.
"""

mylist = ["a", "B", "D", "e", "g", "H"]

def find_upper(x):
  if x == x.upper():
    return x
  
y = filter(find_upper, mylist)
for string in y:
  print(string)