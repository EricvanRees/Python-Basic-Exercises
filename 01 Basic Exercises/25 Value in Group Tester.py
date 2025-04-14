"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

"""

def val_in_list(any_val, any_list):
  if any_val in any_list:
    return True
  else:
    return False
  
print(val_in_list(7, [3,4,5,6,7]))
print(val_in_list(17, [3,4,5,6,7]))
print(val_in_list(77, [3,4,5,6,7]))
print(val_in_list(3, [3,4,5,6,7]))
