"""
Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
"""

def evaluate_input():
  try:
    user_input = int(input("Please enter any integer value: "))
    if type(user_input) == int:
      print("Input is valid integer")
  except ValueError:
    print("Input is not a valid integer")
    
evaluate_input()