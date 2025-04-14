"""
Write a Python program to count the number 4 in a given list.
"""

def four_in_list(a_list):
  if 4 in a_list:
    return True
  else:
    return False
  
print(four_in_list([1,2,3,4]))
print(four_in_list([1,2,3]))
print(four_in_list([3,33,333,3333,33333]))
