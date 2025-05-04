"""
Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
"""

my_list = [1,2,3,4,5,6,7,8,9]

def remove_and_print_thirds(alist):
  # recursive function that deletes every third number of list
  if len(alist) >= 3:
    alist = alist[0:2] + alist[3:]
    print(alist)
    result = remove_and_print_thirds(alist)
  # else statement deletes list elements until list is empty
  else:
    for i in alist:
      del alist[-1]
      result = alist
  return result
  
print(remove_and_print_thirds(my_list))