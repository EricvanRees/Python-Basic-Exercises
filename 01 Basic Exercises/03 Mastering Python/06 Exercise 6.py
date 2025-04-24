"""
Convert a list of integers to a list of booleans where all non-zero values become True.
"""

def true_false(anylist):
  newlist = []
  for num in anylist:
    if num == 0:
      newlist.append(False)
    else:
      newlist.append(True)
      
  return newlist

print(true_false([1,2,3,4,0,0,0]))