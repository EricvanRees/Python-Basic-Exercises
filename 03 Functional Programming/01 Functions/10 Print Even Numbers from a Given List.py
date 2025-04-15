"""
Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""

def print_even(any_list):
  newlist = []
  for i in any_list:
    if i % 2 == 0:
      newlist.append(i)
    else:
      continue
    
  return newlist

print(print_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))