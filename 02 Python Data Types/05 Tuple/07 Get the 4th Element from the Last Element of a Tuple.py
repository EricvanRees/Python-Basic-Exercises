"""
Write a Python program to get the 4th element from the last element of a tuple.
"""

def get_element(atuple):
  return atuple[-1][3]

print(get_element((1,2,3,(1,2,3,4))))