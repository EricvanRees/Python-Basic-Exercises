"""
Write a Python program to find all the values in a list that are greater than a specified number.
"""

def find_vals(alist, anum):
  newlist = []
  for num in alist:
    if num > anum:
      newlist.append(num)
    
  return newlist
    
print(find_vals([1,2,3,4,5], 3))