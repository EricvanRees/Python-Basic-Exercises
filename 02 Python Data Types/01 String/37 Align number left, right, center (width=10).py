"""
Write a Python program to display a number in left, right, and center aligned with a width of 10.
"""

mynumber = 22

print(f"{mynumber:{"@"}<10}")
print(f"{mynumber:{"@"}>10}")
print(f"{str(mynumber).center(10, "@")}")
