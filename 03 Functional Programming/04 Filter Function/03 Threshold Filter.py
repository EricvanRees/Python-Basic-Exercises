"""
Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers using the filter function.
"""

mylist = [1,22,33,44,55,66,77,88]

def less_than(x):
  if x <= 45:
    return x
  
y = filter(less_than, mylist)
for num in y:
  print(num)