"""
Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
"""

def unique_or_not(anylist):
  if len(set(anylist)) == len(anylist):
    print("numbers are different from each other")
  else:
    print("numbers are not different from each other")
    
    

unique_or_not([1,2,3,4])
unique_or_not([1,2,2,4,5])
unique_or_not([1,2,6,7])
