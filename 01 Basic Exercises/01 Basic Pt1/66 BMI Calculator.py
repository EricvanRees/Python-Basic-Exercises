"""
Write a Python program to calculate the body mass index.
"""

def calc_bmi(weight, height):
  return weight / (height ** 2)

print(calc_bmi(90, 1.89))