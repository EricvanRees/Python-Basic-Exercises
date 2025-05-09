"""
Write a Python program that invokes a function after a specified period of time.
"""

import time

def call_later(alist):
  time.sleep(3)
  for i in alist:
    print(i ** 2)
    

call_later([2,3,4])