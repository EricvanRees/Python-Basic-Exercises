"""
Write a Python program to create a tuple with different data types.
"""

def create_tuple(*args):
  mytuple = (args)
  return mytuple

print(create_tuple("a", 1, [1,2,4]))