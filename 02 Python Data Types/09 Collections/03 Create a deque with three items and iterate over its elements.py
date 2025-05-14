"""
Write a Python program to create a new deque with three items and iterate over the deque's elements.
"""
from collections import deque

mylist = ['a', 'e', 'o']

mydeque = deque(mylist)
for item in mydeque:
    print(item)
