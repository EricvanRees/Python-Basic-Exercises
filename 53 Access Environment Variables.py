"""
Write a Python program to access environment variables.

For more information, see https://www.freecodecamp.org/news/python-env-vars-how-to-get-an-environment-variable-in-python/. 
"""

import os

# print all environment vars, returns dict
print(os.environ)

# return value of "PATH" environment var

print(os.environ)["PATH"]
