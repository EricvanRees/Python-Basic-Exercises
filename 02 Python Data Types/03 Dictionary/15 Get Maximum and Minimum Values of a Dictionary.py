"""
Write a Python program to get the maximum and minimum values of a dictionary.
"""

my_dict = {"a": 10, "b": 0, "c": 8}

def return_min_max(mydict):
  sorted_dict = dict(sorted(mydict.items(), key=lambda x:x[1])) 
  min_val = list(sorted_dict.values())[0]
  max_val = list(sorted_dict.values())[-1]
  print(f"min val is {min_val}, max val is {max_val}")
  
return_min_max(my_dict)