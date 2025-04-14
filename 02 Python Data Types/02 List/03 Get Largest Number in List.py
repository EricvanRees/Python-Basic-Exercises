"""
Write a Python program to get the largest number from a list.
"""

def get_largest_num(anylist):
  largest = 0
  for num in anylist:
    if num > largest:
      largest = num
    else:
      continue
    
  return largest

print(get_largest_num([10,2,30,4,5]))