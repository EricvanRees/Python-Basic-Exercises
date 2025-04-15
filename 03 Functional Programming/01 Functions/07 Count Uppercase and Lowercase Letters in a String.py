"""
Write a Python function that accepts a string and counts the number of upper and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

def count_chars(any_string):
  upper = 0
  lower = 0
  for char in any_string:
    if char.isupper():
      upper += 1
    elif char.islower():
      lower += 1
    else:
      continue
  
  print(f"No. of Upper case characters : {upper}\nNo. of Lower case Characters : {lower}")
  
count_chars('The quick Brow Fox')