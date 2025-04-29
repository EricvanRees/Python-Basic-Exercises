"""
Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""

def print_arr(alist):
  list_of_list = []
  for int in alist:
    newstr = "*" * int
    list_of_list.append(newstr)
    
  return list_of_list
  
print(print_arr([3,4,6]))