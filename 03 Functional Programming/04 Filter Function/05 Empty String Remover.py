"""
Write a Python function that filters out all empty strings from a list of strings using the filter function.
"""

mylist = ["", "aaa", "b", "", "d", "nnn", ""]
def newlist(x):
  if x == "":
    pass
  else:
    return x
  
y = filter(newlist, mylist)
for string in y:
  print(string)