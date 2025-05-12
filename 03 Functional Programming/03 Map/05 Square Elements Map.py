"""
Write a Python program to square the elements of a list using the map() function.
"""

def myf(x):
  return x ** 2

mylist  = [10, 30, 40, 50]

y = map(myf, mylist)
print(list(y))
