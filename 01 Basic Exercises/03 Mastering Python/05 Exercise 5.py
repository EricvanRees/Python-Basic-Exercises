"""
Replace all odd numbers in a list with -1.
"""

mylist = [9,7,5,6,4,3]

def oddnrs(alist):
  
  newlist = []
  for i in mylist:
    if i % 2 != 0:
      newlist.append(-1)
    else:
      newlist.append(i)
      
  return newlist

print(oddnrs(mylist))
