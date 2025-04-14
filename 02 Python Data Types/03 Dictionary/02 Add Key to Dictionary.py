"""
Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

mydict = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

def add_key(newkey, newval):
  mydict[newkey] = newval
  return mydict

add_key('Yamal', 14)
print(mydict)