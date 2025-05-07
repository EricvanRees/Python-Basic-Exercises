"""
Given variables x=30 and y=20, write a Python program to print "30+20=50".
"""

def sum_vars(x, y):
  sum_vars = sum([x, y])
  print(f"{x} + {y} = {sum_vars}")
  
sum_vars(30, 20)