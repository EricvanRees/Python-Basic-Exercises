"""
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""

for _ in range(26):
  file_name = str(_) + ".txt"
  file = open(file_name, "w")
  file.write("This is the first line.")
  file.close()
  print(f"Created filename: {file_name}")
  
  