"""
Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
"""

def divide_by(t, n):
  try:
    result = t / n
    print(f"result is {result}")
  except ZeroDivisionError:
    print("Cannot divide by zero")
     

divide_by(2,2)
divide_by(2, 0)