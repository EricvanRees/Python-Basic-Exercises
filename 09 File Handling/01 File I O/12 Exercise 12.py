"""
Write a Python program to write a list to a file.
"""

mylist = ["This","is","some","text"]
mystr = ' '.join(mylist)

f = open("myfile.txt", "x")


with open("myfile.txt", "a") as f:
  f.write(mystr)