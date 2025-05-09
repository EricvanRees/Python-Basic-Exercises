"""
Write a Python program to execute a string containing Python code.
"""

def run_str(astr):
  return exec(astr)

mystr = "print(15)"
print(run_str(mystr))

