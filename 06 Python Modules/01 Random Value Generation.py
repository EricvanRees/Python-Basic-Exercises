"""
Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()
"""

import random

hexvals = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def create_hexval():
  random_color_hex = "#"
  i = 1
  while i < 7:
    randomint = random.randint(1, 15)
    random_color_hex += hexvals[randomint]
    i += 1
  
  return random_color_hex
  

print(create_hexval())
print(create_hexval())
print(create_hexval())
print(create_hexval())
