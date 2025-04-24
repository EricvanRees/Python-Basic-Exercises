"""
Create a 3x3 list of lists with random values and normalize it.
"""

import random

def normalize_lists():  
  # create 3 lists of 3 random integers each   
  list_of_lists = [[random.randint(1,100) for i in range(3)] for j in range(3)]
  # create empty new lists for 3 normalized lists
  new_list_of_lists = []   
  # iterate over each list and normalize each element
  for list in list_of_lists:
    newlist = []
    for i in list:
      i_normalized = (i - min(list)) / (max(list) - min(list))
      # append normalized element to new list
      newlist.append(i_normalized)
    # append normalized list elements to list of lists  
    new_list_of_lists.append(newlist)
  print(new_list_of_lists)

normalize_lists()
    