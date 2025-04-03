"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def number_tester(a_num):
  if a_num >= 900 and a_num <= 1100:
    return True
  elif a_num >= 1900 and a_num <= 2100:
    return True
  else:
    return False
  

print(number_tester(1200))
print(number_tester(2100))
print(number_tester(2000))
print(number_tester(2200))
