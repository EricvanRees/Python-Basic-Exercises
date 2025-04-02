"""
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""

import calendar

def print_calendar(year, month):
  print(calendar.month(year, month))

print_calendar(2025, 4)