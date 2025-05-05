"""
Write a Python program that creates a list of dictionaries containing student information (name, age, grade) and uses the filter function to extract students with a grade greater than or equal to 95.
"""

import random

def filter_grades():
  
  mylist = ["Jan", "Piet", "Klaas"]
  list_of_dicts = []
  for name in mylist:
    newdict = {}
    newdict[name] = {"Age": 23, "Grade": random.randint(55,99)}
    list_of_dicts.append(newdict)
  
  return filter_grade(list_of_dicts)
  
def filter_grade(list_of_dicts):
  for d in list_of_dicts:
    for value in d.values():
      if value["Grade"] >= 95:
        list_of_dicts.remove(d)
      
  return list_of_dicts
      
print(filter_grades())