"""
Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
"""

def perform_action(myvar):
  if myvar == 1:
    print("First day of a Month!")
  else:
    return False
  
perform_action(1)
perform_action(2)
perform_action(3)