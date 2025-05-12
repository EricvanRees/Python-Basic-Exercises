"""
Write a Python function to reverse a string if its length is a multiple of 4.
"""

def reverse_str(astr):
  if len(astr) % 4 == 0:
    return astr[::-1]
  else:
    return astr
  
print(reverse_str("1234"))
print(reverse_str("abcdabcdabcd"))