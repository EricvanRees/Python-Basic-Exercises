"""
Write a Python program to iterate over dictionaries using for loops.
"""

def iterate(mydict):
  for k, v in mydict.items():
    print(k, v)
    
mydict = {"a": 1, "b": 2, "c": 3, "d": 4}
iterate(mydict)