"""
Find the indices of non-zero elements in a list.
"""

def find_non_zeros(alist):
  y = enumerate(alist)
  for index, num in y:
    if num != 0:
      print(index)
    
print(find_non_zeros([0,1,2,3,4,0,5,6,7,0,8,9,0]))