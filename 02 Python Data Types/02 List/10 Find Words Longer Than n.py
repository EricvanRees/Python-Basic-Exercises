"""
Write a Python program to find the list of words that are longer than n from a given list of words.
"""

def longer_than_n(anylist, n):
  newlist = [item for item in anylist if len(item) > n]
  print(newlist)
  
longer_than_n(["abc", "defg", "aaaaa", "b"], 2)

  