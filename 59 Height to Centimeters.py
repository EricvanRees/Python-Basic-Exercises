"""
Write a Python program to convert height (in feet and inches) to centimeters.
"""

def convert_height(anum, measurement_unit):
  if measurement_unit == "feet":
    cm = round((anum / 3.281) * 100, 2)
    return f"{anum} feet is {cm} cm"
  elif measurement_unit == "inches":
    cm = round((anum / 39.37) * 100, 2)
    return f"{anum} inches is {cm} cm"
  else:
    return False
  

print(convert_height(100, "feet"))
print(convert_height(100, "inches"))