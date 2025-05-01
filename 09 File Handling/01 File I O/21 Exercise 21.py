"""
Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.
"""

file_name= "my_file.txt"

#open file in "write" mode
with open(file_name, 'w') as file:
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in range(26):
    file.write(str(alphabet[i]*(i + 1)) +"\n")
  
  print(f"Created file {file_name}")