"""
Write a Python function that checks if a given list is empty or not using boolean logic.
"""

def empty_or_not(alist):
  if len(alist) == 0:
    return True
  
  
def return_str(alist):
  if (empty_or_not(alist)):
    print("List is empty")
  else:
    print("List is not empty")
    
return_str([1,2,3])
return_str([3])
return_str([])