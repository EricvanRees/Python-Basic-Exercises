"""
Write a Python program to concatenate N strings.
"""

def concat_str(*args):
  newstr = ''
  for arg in args:
    newstr += arg
    
  return newstr

print(concat_str("a", "b", "c", "d", "e", "f"))