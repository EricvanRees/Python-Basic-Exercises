"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""

def print_docstr(myf):
  print(myf. __doc__ )

print_docstr(abs)
