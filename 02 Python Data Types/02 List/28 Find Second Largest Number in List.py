"""
Write a Python program to find the second largest number in a list.
"""

def find_2nd_largest_nr(alist):
  sorted_list = sorted(alist)
  return f"2nd largest number in list is {sorted_list[-2]}"

mylist = [1,2,3,4]
print(find_2nd_largest_nr(mylist))