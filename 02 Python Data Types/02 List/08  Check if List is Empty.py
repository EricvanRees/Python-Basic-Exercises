"""
Write a Python program to check if a list is empty or not.
"""

def check_length(anylist):
  if len(anylist) == 0:
    return "list is empty"
  else:
    return "list is not empty"
  
print(check_length([]))
print(check_length([1,2,3]))
print(check_length([1,2]))
print(check_length([0]))
print(check_length([]))