"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

Sample Output:
25
48
"""

x = lambda a : a + 15
print(x(5))

x = lambda a, b : a * b 
print(x(5, 6))