"""
Write a Python program to create a tuple of numbers and print one item.
"""

def create_tuple(*args):
  mylist = []
  for arg in args:
    if type(arg) == int:
      mylist.append(arg)
    else:
      continue
  
  mytuple = tuple(mylist)  
  print(mytuple[0])
  

create_tuple(1,2,3,4)