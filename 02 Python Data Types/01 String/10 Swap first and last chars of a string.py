"""
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""

def swap_str(astr): 
  newstr = astr[-1] + astr[1:-1] + astr[0]
  return newstr

print(swap_str("abc"))
print(swap_str("Amsterdam"))