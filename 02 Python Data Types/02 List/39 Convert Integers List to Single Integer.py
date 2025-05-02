"""
Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
"""

def convert_ints(alist):
  newint = ''
  for item in alist:
    newint += str(item)
    
  return newint

print(convert_ints([11, 33, 50]))