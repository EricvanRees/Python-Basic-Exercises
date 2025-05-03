"""
Write a Python program to create a list of empty dictionaries.
"""

def list_of_dicts():
  newlist = []
  for i in range(3):
    newlist.append({})
    
  return newlist

print(list_of_dicts())