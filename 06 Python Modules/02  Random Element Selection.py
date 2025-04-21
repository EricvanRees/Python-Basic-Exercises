"""
Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory. Use random.choice()
"""

import random

def select_from_list():
  mylist = [1,2,3,4,5,6]
  return random.choice(mylist)

print(select_from_list())
print(select_from_list())
print(select_from_list())
print(select_from_list())