"""
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import datetime

def day_diff(date1, date2):

  # convert tuple items to list of strings
  date1_list = list(map(str, date1))
  date2_list = list(map(str, date2))
  # convert list of strings to single string with "/" as separator
  date1_str = "/".join(date1_list)
  date2_str = "/".join(date2_list)
  
  # convert tuple to date object
  d1 = datetime.strptime(date1_str, "%Y/%m/%d")
  d2 = datetime.strptime(date2_str, "%Y/%m/%d")

  # difference between dates in timedelta
  delta = d2 - d1
  print(f'Difference is {delta.days} days')

day_diff((2014, 7, 2), (2014, 7, 11))
