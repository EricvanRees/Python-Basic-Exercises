"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""

mydict = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted by value ascending
sorted_by_val = dict(sorted(mydict.items(), key=lambda x:x[1]))
print(sorted_by_val)

# sorted by value descending
sorted_by_val_desc = dict(sorted(mydict.items(), key=lambda x:x[1], reverse=True))
print(sorted_by_val_desc)

