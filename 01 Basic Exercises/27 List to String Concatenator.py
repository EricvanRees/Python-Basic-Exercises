"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

def concat_list(any_list):
  newstr= ''
  for el in any_list:
    newstr += str(el)

  return newstr

print(concat_list([1,2,3,4]))
print(concat_list(["b", "c", "d", "e"]))