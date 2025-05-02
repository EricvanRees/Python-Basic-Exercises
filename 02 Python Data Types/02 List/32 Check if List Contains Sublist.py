"""
Write a Python program to check whether a list contains a sublist.
"""

def check_for_sublist(alist):
  for el in alist:
    if type(el) == list:
      print("list contains sublist")
    else:
      continue
    
check_for_sublist([1,2,3,[1,2,3,4],5,6])