"""
Write a Python program to get the current value of the recursion limit.
"""

import sys

limit = sys.getrecursionlimit()
print(f"Current recursion limit is {limit}.")