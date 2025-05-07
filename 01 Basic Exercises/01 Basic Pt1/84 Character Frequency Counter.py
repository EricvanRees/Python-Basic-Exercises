"""
Write a Python program to count the number of occurrences of a specific character in a string.
"""

def count_substr(string, substr):
  return string.count(substr)

print(count_substr("abcdeeeeeffffhhhh", "e"))