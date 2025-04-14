"""
Write a Python script to check whether a given key already exists in a dictionary.
"""

mydict = {"a":1, "b":2, "c":3}

def check_key(anykey):
  if anykey in mydict.keys():
    return True
  else:
    return False
  
print(check_key("a"))
print(check_key("b"))
print(check_key("c"))
print(check_key("d"))