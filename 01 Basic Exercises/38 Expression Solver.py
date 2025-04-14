"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

def expression_solver(x, y):
  return (x + y) ** 2

print(expression_solver(4, 3))
print(expression_solver(3, 3))
print(expression_solver(2, 2))
print(expression_solver(1, 3))