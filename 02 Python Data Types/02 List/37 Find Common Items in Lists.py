"""
Write a Python program to find common items in two lists.
"""

def compare_lists(a, b):
  common_items = []
  for i in a:
    for j in b:
      if i == j:
        common_items.append(i)
      else:
        continue
  
  return common_items

print(compare_lists([1,2,3,4],[3,4,5,6]))