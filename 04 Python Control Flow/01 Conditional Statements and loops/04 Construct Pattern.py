"""
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

def print_diamond():
  for i in range(1,10):
    if i <= 5:
      print(i * '* ')
    else:
      print((10 - i) * '* ')
    
    
print_diamond()