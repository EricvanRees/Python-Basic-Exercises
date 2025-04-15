"""
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

see:https://geekflare.com/dev/prime-number-in-python/ 
"""

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print(is_prime(8))