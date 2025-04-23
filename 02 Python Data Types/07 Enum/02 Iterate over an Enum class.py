"""
Iterate over an Enum class and display members and values
"""

from enum import Enum

class Country(Enum):
  Afghanistan = 93
  Albania = 355
  Algeria = 213
  Andorra = 376
  Angola = 244
  Antarctica = 672
  
for data in Country:
  print(data.name, data.value)