"""
Write a Python program to parse a string to float or integer.
"""

def parse_str(any_str):
  if "." in any_str:
    return float(any_str)
  else:
    return int(any_str)


print(parse_str("444"))
print(parse_str("444.99"))
print(parse_str("444.0"))