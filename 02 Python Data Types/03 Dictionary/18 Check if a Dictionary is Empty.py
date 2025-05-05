"""
Write a Python program to check if a dictionary is empty or not.
"""

def check_length(adict):
  if len(adict) == 0:
    print(f"dictionary is empty")
  else:
    print(f"dictionary is not empty")
    
mydict = {}
check_length(mydict)