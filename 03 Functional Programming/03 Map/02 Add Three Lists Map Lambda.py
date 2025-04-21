"""
Write a Python program to add three given lists using Python map and lambda.
"""

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

myfunc = lambda i, j, k: (i + j + k)
y = list(map(myfunc, a, b, c))
print(y)
