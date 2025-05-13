"""
Write a Python program to check whether an element exists within a tuple.
"""

def check_element(atuple, el):
  if el in atuple:
    return True
  else:
    return False
  
print(check_element((1,2,3,4), 4))