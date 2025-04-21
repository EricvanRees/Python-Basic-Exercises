"""
Write a Python program to listify the list of given strings individually using Python map.
"""

mylist = ["Red", "Green", "Blue"]

def split(item):
    return list(item)
  
y = map(split, mylist)
print(list(y))