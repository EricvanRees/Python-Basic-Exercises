"""
Calculate the dot product of two lists.
"""
import math

list1 = [1,2,3]
list2 =  [4,5,6]

def calc_dot_pr(lista, listb):
  total = 0
  newlist = zip(lista, listb)
  list_of_tuples = list(newlist)
  for item in list_of_tuples:
    total += math.prod(item)
    
  return total
 
print(calc_dot_pr(list1, list2))