"""
Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
"""

import random

x = lambda a : a * random.randint(2, 5)
print(x(5))