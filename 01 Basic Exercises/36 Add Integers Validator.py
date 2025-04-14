"""
Write a Python program to add two objects if both objects are integers.
"""

def int_check(int1, int2):
  if type(int1) == int and type(int2) == int:
    return int1 + int2
  else:
    return False
  
print(int_check(2, 3)) 
print(int_check(21, 3)) 
print(int_check(24, 3))
print(int_check("2", "3"))
 