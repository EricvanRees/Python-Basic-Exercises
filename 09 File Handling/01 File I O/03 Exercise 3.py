"""
Write a Python program to append text to a file and display the text.
"""

print("***Append info to file***")

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

with open(file_name, 'a') as file:
  # append info
  file.write("\nAppending info...\n")
  file.write("Exiting appending info...\n")

print(f'Appended info to file {file_name}')