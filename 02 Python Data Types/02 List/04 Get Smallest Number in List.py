"""
Write a Python program to get the smallest number from a list.
"""

def get_smallest(anylist):
  smallest = 0
  for num in anylist:
    if num < smallest:
      smallest = num
    else:
      continue
    
  return smallest

print(get_smallest([10, -100, 20, -20]))