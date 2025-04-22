"""
Convert a list of integers to a list of strings.
"""

mylist = [1,2,3,4,5,6]

newlist = []
for i in mylist:
  newlist.append(str(i))
  
print(newlist)