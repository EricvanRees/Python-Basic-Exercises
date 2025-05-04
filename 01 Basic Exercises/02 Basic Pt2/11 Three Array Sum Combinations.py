"""
Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
Sample data:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
*/
"""

def check_sum(a, b, c, target_val):
  if sum(a) == target_val:
    print(f"sum of {a} is equal to target value {target_val}")
  elif sum(b) == target_val:
    print(b)
  elif sum(c) == target_val:
    print(c)
    
  else:
    print("No match")
    
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70

check_sum(X, Y, Z, target)