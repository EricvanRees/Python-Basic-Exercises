"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

def remove_els(alist):
  newlist = alist[:]
  for index, val in enumerate(alist):
    if index == 0 or index == 4 or index == 5:
      newlist.remove(val)
    
  return newlist

print(remove_els(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))