"""
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""

def find_multiples():
  newlist = []
  for i in range(1500,2700):
    
    if i % 7 == 0:
      if i % 5 == 0:
        newlist.append(i)
    else:
      continue
    
  return newlist

print(find_multiples())