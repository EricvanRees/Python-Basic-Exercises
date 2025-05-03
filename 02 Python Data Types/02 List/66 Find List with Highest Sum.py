"""
Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

def find_highest_sum(a, b, c, d):
  if sum(a) > sum(b) and sum(a) > sum(c) and sum(a) > sum(d):
    return a
  elif sum(b) > sum(a) and sum(b) > sum(c) and sum(b) > sum(d):
    return b
  elif sum(c) > sum(a) and sum(c) > sum(b) and sum(c) > sum(d):
    return c
  else:
    return d
  
a, b, c, d = [1,2,3], [4,5,6], [10,11,12], [7,8,9]
print(find_highest_sum(a, b, c, d))
  