"""
Extract all odd numbers from a list of integers.
"""

mylist = [9,8,6,5,3,1]
newlist = []

def filter_list(mylist):
  for i in mylist:
    if i % 2 == 0:
      newlist.append(i)
    else:
      continue
    
  return newlist

print(filter_list(mylist))
