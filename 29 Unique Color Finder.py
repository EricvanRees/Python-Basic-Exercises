"""
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

def compare_sets(set1, set2):
  newSet = []
  for item in set1:
    if item in set2:
      continue
    else:
      newSet.append(item)
  return set(newSet)

print(compare_sets({"White", "Black", "Red"}, {"Red", "Green"}))