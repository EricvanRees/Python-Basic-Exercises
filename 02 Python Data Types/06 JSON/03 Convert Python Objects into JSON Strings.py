"""
Write a Python program to convert Python objects into JSON strings. Print all the values.
"""

import json

python_objects = [{"a": 124, "b": "python", "c": 345}, {"b": 999, "dd": "098", "ddd": "0987"}]

json_objects = [json.dumps(item) for item in python_objects]
print(json_objects)