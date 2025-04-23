"""
Write a Python program to create an Enum object and display a member name and value.

Sample data :
Member name: Albania
Member value: 355
"""

from enum import Enum

class Country(Enum):
  Afghanistan = 93
  Albania = 355
  Algeria = 213
  Andorra = 376
  Angola = 244
  Antarctica = 672
  
print(Country.Albania.value)