"""
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
"""

def n_copies_of_str(n, a_str):
  if n >= 2:
    return n * a_str[:2]
  else:
    return n * a_str

print(n_copies_of_str(1, "abc"))
print(n_copies_of_str(4, "abc"))