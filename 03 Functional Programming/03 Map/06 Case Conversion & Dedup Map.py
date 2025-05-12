"""
Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
"""

mylist = ["a", "b", "c", "a", "b", "c"]
def myf(x):
  if x.islower():
    return x.upper()

y = map(myf, mylist)
print(set(y))