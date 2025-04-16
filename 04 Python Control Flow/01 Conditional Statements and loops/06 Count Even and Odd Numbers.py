"""
Write a Python program to count the number of even and odd numbers in a series of numbers.
"""

def count_even_odd(anum):
  odd = 0
  even = 0
  anum = str(anum)
  for num in anum:
    if int(num) % 2 == 0:
      even += 1
    else:
      odd += 1
      
  print(f'Even number count: {even}, odd number count: {odd}.')
  
count_even_odd(10987345)