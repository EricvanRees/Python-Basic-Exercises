"""
Multiply all elements in a list by 2.
"""

mylist = [2,4,6,8]
newlist = []
for i in mylist:
  i *= 2
  newlist.append(i)
  
print(newlist)