"""
Write a Python program to remove a newline in Python.
"""

mystr = "This is a sentence. \nHere starts a newline."

def del_newline(astr):
  pos = astr.find("\n")
  return astr[0:pos -1 ] + " " + astr[pos + 1:]
  
print(del_newline(mystr))