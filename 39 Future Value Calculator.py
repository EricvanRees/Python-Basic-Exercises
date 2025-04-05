"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

def calc_future_value(amt, int, years):
  return amt * (((1 + ((int/100.0))) ** (years)))


print(calc_future_value(10000, 3.5, 7))