"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

def del_even_nrs(alist):
  newlist = alist[:]
  for num in newlist:
    if num % 2 == 0:
      newlist.remove(num)
    
  return newlist

print(del_even_nrs([1,2,3,4,5,6,7,8]))