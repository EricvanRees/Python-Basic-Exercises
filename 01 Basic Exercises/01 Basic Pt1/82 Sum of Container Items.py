"""
Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
"""

def sum_of_cont(item):
  if type(item) == list:
    return sum(item)
  elif type(item) == tuple:
    return sum(list(item))
  elif type(item) == set:
    return sum(item)
  elif type(item) == dict:
    return sum(item.values())
  else:
    return False
 
print(sum_of_cont([1,2,3,4,5])) 
print(sum_of_cont((2,3,4,5))) 
print(sum_of_cont({2,3,4,5})) 
print(sum_of_cont({"a": 1, "b": 2, "c": 3})) 
  