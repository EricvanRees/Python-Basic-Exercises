"""
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

def str_count(anylist):
  count = 0
  for str in anylist:
    if len(str) >= 2 and str[0] == str[-1]:
      count += 1
    
  return count

print(str_count(['abc', 'xyz', 'aba', '1221']))