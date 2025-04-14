"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

def count_chars(anystr):
  return {x:anystr.count(x) for x in anystr}
    

print(count_chars("google.com"))