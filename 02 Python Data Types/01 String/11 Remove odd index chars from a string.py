"""
Write a Python program to remove characters that have odd index values in a given string.
"""


def remove_odd_chars(astr):
  newstr = ''
  for i, val in enumerate(list(astr)):
    if i % 2 == 0:
      newstr += val
      
  print(newstr)
    

remove_odd_chars("abcdefghijklmnopqrstuvwxyz")