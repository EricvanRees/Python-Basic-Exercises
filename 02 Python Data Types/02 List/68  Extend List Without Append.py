"""
Write a Python program to extend a list without appending.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
"""

def grow_list(a, b):
  return [j for i in [a, b] for j in i]      
  
a, b = [10, 20, 30], [40, 50, 60]
print(grow_list(a, b))