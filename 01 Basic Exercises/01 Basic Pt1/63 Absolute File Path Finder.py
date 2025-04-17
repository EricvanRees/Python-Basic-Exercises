"""
Write a Python program to get an absolute file path.
"""

import os

file_path = os.path.realpath(__file__)
print(file_path)