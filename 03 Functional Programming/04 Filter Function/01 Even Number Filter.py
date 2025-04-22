"""
Write a Python function that filters out even numbers from a list of integers using the filter function.
"""

int_list = [3,4,5,6,7,8]

def even(x):
  if x % 2 == 0:
    return x
  
y = filter(even, int_list)
for num in y:
  print(num)
  
