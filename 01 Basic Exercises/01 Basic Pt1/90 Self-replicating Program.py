"""
Write a Python program to create a copy of its own source code.
"""
import copy

def myfunction():
  print("Hello world!")


mycopy = myfunction()
anothercopy = copy.copy(mycopy)
print(anothercopy)