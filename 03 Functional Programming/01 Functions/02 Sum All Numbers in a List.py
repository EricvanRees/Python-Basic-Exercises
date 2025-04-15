"""
Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

def sum_nums(*args):
  sum = 0
  for arg in args:
    sum += arg
    
  return sum

print(sum_nums(2,3,4,5))