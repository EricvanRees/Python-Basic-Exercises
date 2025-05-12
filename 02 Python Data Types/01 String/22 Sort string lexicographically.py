"""
Write a Python program to sort a string lexicographically.
"""

def sort_lexico(astr):
  return sorted(astr, key=str.upper)
      
      
print(sort_lexico("W3resource"))