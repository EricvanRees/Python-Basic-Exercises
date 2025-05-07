"""
Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def find_subst(astr, substr1, substr2):
  newstr = substr1 + substr2
  if astr.find(substr1):
    if astr.find(substr2):
      index = astr.find(substr1)
      return astr[0:index] + substr2
  
print(find_subst("The lyrics is not that poor!", "not", "poor"))