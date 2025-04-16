"""
Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
"""

class Calculator:
  def __init__(self):
    pass
    
  def add(self, a, b):
             
    return a + b
  
  def subtract(self, a, b):
    
    return a - b 
  
  def multiply(self, a, b):
    
    return a * b
  
  def division(self, a, b):
    
    return a / b
  
  
mycalc = Calculator()
print(mycalc.add(2, 3))
print(mycalc.subtract(2, 3))
print(mycalc.multiply(2, 3))
print(mycalc.division(21, 3))