"""
Write a Python program to sum all the items in a dictionary.
"""

mydict = {"a": 1, "b": 2, "c": 3, "d": 4}

def return_sum(adict):
  sum = 0

  for k, v in mydict.items():
    sum += v
  
  return sum

print(return_sum(mydict))