"""
Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3
"""
import math


def area_vol_calc(l, w, r, h):
    area = l * w
    vol = math.pi * (r * r) * h
    return f"area is {area}cm2, cylinder volume is {vol:.2f}cm3."


print(area_vol_calc(1, 3, 5, 6))
