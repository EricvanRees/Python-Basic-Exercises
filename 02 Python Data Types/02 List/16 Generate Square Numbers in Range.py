"""
Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
"""

import random

def square_list():  
  newlist = []
  for i in range(30):
    i = random.randint(1,30)
    i *= i
    newlist.append(i)
  
  mylist = newlist[0:5] + newlist[-5:]
  return mylist

print(square_list())