"""
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""

from datetime import date

class Person:
  def __init__(self, name, country, date_of_birth):
    self.name = name
    self.country = country
    self.date_of_birth = date_of_birth
    
  def age(self):
    # Get the current date
      current_date = date.today()
      # Access the year attribute to get the current year
      current_year = current_date.year
      return int(current_year) - int(self.date_of_birth[0:4])
    
    
me = Person('Eric', 'Holland', '1980-5-2')
print(me.age())