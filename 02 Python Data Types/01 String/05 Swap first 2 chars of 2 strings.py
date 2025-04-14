"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

def newstr(string1, string2):
  return string2[0:2] + string1[2:] + " " + string1[0:2] + string2[2:]

print(newstr('abc', 'xyz'))