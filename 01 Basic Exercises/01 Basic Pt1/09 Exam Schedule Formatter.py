"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

def format_tuple(atuple):
  return f"{atuple[0]} / {atuple[1]} / {atuple[2]}"

print(format_tuple((11, 12, 2014)))