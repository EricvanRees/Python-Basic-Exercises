"""
Find the index of the maximum value in a list.
"""

def find_max_index(alist):
  newlist = enumerate(alist)
  print(max(newlist)[0])
    
find_max_index([1,2,3,4,5])