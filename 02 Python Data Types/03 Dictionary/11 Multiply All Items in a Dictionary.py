"""
Write a Python program to multiply all the items in a dictionary.
"""

mydict = {"a": 1, "b": 2, "c": 3, "d": 4}

def multiply_items(adict):
  sum = 1

  for k, v in mydict.items():
    sum = sum * v
  
  return sum

print(multiply_items(mydict))