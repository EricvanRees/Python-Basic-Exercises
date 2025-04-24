"""
Create a 3x3 list of lists with random values and normalize it.
"""

alist = [[2,4,10,6,8,4],[2,4,10,6,8,4],[2,4,10,6,8,4]]

def normalize(alist):
  list_of_lists = []
 
  for list in alist:
    newlist = []
    for i in list:
      i_normalized = (i - min(list)) / (max(list) - min(list))
      newlist.append(i_normalized)
    
    list_of_lists.append(newlist) 
  return list_of_lists

print(normalize(alist))
    