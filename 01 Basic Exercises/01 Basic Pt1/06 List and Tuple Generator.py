"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

def tuple_list(*args):
  return f"List: {list(args)}\nTuple: {tuple(args)}"


print(tuple_list(1,3,4))