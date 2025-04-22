"""
Write a Python program to create a decorator that logs the arguments and return value of a function.
"""

def decorator(func):
  def wrapper(*args):
    print(*args)
    result = func(*args)
    return result
  return wrapper

@decorator
def myf(a, b):
  return a * b

print(myf(1, 3))

