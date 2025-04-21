"""
Write a Python program to calculate the midpoints of a line.
"""

def calc_midpoint(a, b):
  m = ((a[0] + b[0]) / 2, ((a[1] + b[1]) / 2))
  return m 

print(calc_midpoint((-1, 2), (3, -6)))

     
