"""
Write a Python program to remove duplicates from a list.
"""

my_list = [1,2,3,4,4,4,4]

def remove_duplicates(anylist):
  return set(anylist)

print(remove_duplicates(my_list))