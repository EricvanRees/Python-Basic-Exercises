"""
Write a Python program to add an item to a tuple
"""

def add_item(mytuple, item_to_add):
  newlist = list(mytuple)
  newlist.append(item_to_add)
  return tuple(newlist)

print(add_item((1,2,3), 4))