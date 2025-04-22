"""
Write a Python program that creates a list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U).
"""

import random

mylist = ["Andre", "Eric", "Peter", "Iris", "Otto", "Egbert", "Frida", "Jan"]

def new_list(x):
  vowels = "AEIOUaeiou"
  for vowel in vowels:
    if x.startswith(vowel):
      return x
    
y = filter(new_list, mylist)
for name in y:
  print(name)
  
    