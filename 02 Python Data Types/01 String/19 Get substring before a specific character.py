"""
Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
"""

def get_last_part(astr, char):
  mylist = astr.split(char)
  return mylist[0]

print(get_last_part("https://www.w3resource.com/python-exercises", "-"))

