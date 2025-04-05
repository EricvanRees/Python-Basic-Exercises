"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

def calc_dist(a, b):
  hor_dist = b[0] - a[0]
  vert_dist = b[1] - a[1]
  return (hor_dist, vert_dist)

print(calc_dist((1,1), (4,8)))