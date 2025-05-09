"""
Write a Python program to find the median among three given numbers.
"""

def find_median(alist):
  if len(alist) == 3:
    return sorted(alist)[1]

print(find_median([2,5,1]))