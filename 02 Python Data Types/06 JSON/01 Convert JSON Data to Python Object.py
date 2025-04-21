"""
Write a Python program to convert JSON data to Python object.
"""

import json

json_obj = '{"a": "abc", "b": "890", "c": "New York"}'

python_obj = json.loads(json_obj)
print(python_obj)