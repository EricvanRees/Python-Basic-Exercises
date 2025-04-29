"""
Write a Python function that takes two lists and returns True if they have at least one common member.
"""

def compare_lists(a, b):
  newlist = a + b
  if set(newlist) == newlist:
    return False
  else:
    return True
 
      
print(compare_lists([1,2,3],[2,3,4]))