"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

def number_expansion(n):
  return int(str(n)) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))

print(number_expansion(5))