"""
Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory. Use random.choice()
"""

import random, os

def select_from_list():
  mylist = [1,2,3,4,5,6]
  return random.choice(mylist)

def select_from_set():
  myset = {1,2,3,4,5,6}
  return random.choice(list(myset))

def select_val_from_dict():
  mydict = {1: "a", 2: "b", 3: "c", 4: "d"}
  return random.choice(list(mydict.values()))

def select_file_from_dir():
  myPath = r"C:\\Users\\mipc\\Downloads\\OneDrive_1_14-4-2025"
  arr = os.listdir(myPath)
  print(random.choice(arr))


select_file_from_dir()