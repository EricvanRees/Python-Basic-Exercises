"""
Replace all even numbers in a list with their negative.
"""

def change_even(alist):
  newlist =[]
  for item in alist:
    if item % 2 == 0:
      newlist.append(-item)
    else:
      newlist.append(item)
      
  return newlist

print(change_even([1,2,3,4,5]))