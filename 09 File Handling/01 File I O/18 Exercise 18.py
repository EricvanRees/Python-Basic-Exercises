"""
Write a Python program that takes a text file as input and returns the number of words of a given text file.
"""

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

def count_words(my_file):
  word_count = 0
  with open(my_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      for word in line.split():
        word_count += 1
        
  print(f"word count is {word_count}")

count_words(file_name)