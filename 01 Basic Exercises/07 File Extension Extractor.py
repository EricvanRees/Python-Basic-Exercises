"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

def filename_extr(filename):
  return filename.split(".")[1]

print(filename_extr("abc.java"))