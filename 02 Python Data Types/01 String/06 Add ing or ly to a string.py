"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def add_to_string(astring):
  if len(astring) >= 3:
    if astring[-2:] == 'ing':
      return astring + 'ly'
    else:
      return astring + 'ing'
  else:
    return astring
  
print(add_to_string('abc')) 
print(add_to_string('string')) 