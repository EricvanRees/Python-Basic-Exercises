"""
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""

def rev_name(name):
  name = name[::-1]
  newstr = ''
  for i in name:
    i += " "
    newstr += i
  return newstr

print(rev_name("name"))
