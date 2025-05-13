"""
Write a Python program to remove an item from a tuple.
"""

def remove_item(atuple, item):
  if item in atuple:
    mylist = list(atuple)
    mylist.remove(item)
    mytuple = tuple(mylist)
    
  return mytuple

print(remove_item((1,2,3,4), 4))
    