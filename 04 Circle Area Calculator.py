"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math

def calc_area(radius):
  # area = pi* (r**2)
  area = math.pi * (radius * radius)
  return f"area is {area}"

print(calc_area(1.1))