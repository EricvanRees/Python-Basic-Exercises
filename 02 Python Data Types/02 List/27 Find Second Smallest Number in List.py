"""
Write a Python program to find the second smallest number in a list.
"""

def find_2nd_smallest_nr(alist):
  sorted_list = sorted(alist)
  return f"2nd smallest number in list is {sorted_list[1]}"

mylist = [1,2,3,4]
print(find_2nd_smallest_nr(mylist))