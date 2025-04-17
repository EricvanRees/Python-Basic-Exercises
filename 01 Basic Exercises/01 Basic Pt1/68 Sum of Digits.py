"""
Write a Python program to calculate sum of digits of a number.
"""

def digits_sum(anum):
  # list comprehension for turning int into single digits
  stringed = [int(d) for d in str(anum)]
  mysum = sum(stringed)
  print(mysum)
  
digits_sum(5432)