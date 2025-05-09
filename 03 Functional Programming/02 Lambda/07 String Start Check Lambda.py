"""
Write a Python program to find if a given string starts with a given character using Lambda.

Sample Output:
True
False
"""
mystring = "karperzooi"
mybool = lambda x: True if mystring[0] == 'k' else False
print(mybool(mystring))

