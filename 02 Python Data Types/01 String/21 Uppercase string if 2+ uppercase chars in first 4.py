"""
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
"""

def count_upper(astr):
  newstr = astr[0:4]
  count = 0
  for letter in newstr:
    if letter.isupper():
      count += 1
      
  if count >= 2:
    return astr.upper()
  else:
    return astr
  
print(count_upper("abracadabra"))
print(count_upper("ABracadabra"))
print(count_upper("AbracAdabra"))