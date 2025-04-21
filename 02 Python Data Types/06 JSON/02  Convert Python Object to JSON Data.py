"""
Write a Python program to convert Python object to JSON data.
"""

import json

python_obj = {"a": 124, "b": "python", "c": 345}

json_obj = json.dumps(python_obj)
print(json_obj)