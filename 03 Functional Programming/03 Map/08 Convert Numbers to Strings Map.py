"""
Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
"""

mylist = [1,2,3,4]


y = list(map(str, mylist))
z = tuple(map(str, mylist))
print(y, z)