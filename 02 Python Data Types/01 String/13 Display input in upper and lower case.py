"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""

def input_lower_upper():
  user_input = str(input("Enter text: "))
  print(user_input.lower(), user_input.upper())
  
  
input_lower_upper()