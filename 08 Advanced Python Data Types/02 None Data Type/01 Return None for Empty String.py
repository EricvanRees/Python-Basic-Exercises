"""
Write a Python function that takes a string as input and returns "None" if the string is empty, otherwise it returns the given string.
"""

def string_or_none(astring):
  if not astring.strip():
    return None
  else:
    return astring
  
print(string_or_none("2"))
print(string_or_none(""))
print(string_or_none("22"))
print(string_or_none('  '))