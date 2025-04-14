"""
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""

def add_is(any_str):
  if any_str.startswith('Is'):
    return any_str
  else:
    return "Is" + any_str
  

print(add_is("Isokokok"))
print(add_is("notok"))