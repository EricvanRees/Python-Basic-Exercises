"""
Write a Python program to remove the nth index character from a nonempty string.
"""

def remove_nth_char(astr):
  if len(astr) >= 3:
    return astr[0:2] + astr[3:]
  else:
    return astr
  
print(remove_nth_char("@@a@@@"))
print(remove_nth_char("@@@"))