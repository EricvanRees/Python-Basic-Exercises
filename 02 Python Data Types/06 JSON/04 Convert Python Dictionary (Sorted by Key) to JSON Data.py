"""
Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
"""

import json

mydict = {1: "c", 42: "d", 3: "ff"}
sorted_dict = sorted(mydict.items())
json_sort = json.dumps(sorted_dict)
print(json_sort)
