"""
Write a Python function to multiply all the numbers in a list.

Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

def multiply_nums(*args):
  total = 1
  for arg in args:
    total *= arg
    
  return total

print(multiply_nums(8, 2, 3, -1, 7))
