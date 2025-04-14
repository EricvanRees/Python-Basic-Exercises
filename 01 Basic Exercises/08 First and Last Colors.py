"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""

def first_last_color(alist):
  return alist[0], alist[-1]

color_list = ["Red","Green","White" ,"Black"]
print(first_last_color(color_list))