"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def newstr(anystr):  
  return anystr[0] + anystr.replace(anystr[0], '$')[1:]

print(newstr('restart'))