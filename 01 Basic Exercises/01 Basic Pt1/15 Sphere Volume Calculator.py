"""
Write a Python program to get the volume of a sphere with radius six.
"""

import math

def vol_sphere(r):
  vol = 4/3 * math.pi * (r**3)
  print("{:.2f}".format(vol))

vol_sphere(6)
