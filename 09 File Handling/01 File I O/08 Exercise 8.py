"""
Write a python program to find the longest words.
"""

def find_longest_word(my_file):
  word_length = {}
  with open(my_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      for word in line.split():
        word_length[word] = len(word)
  
  longest_word = word_length.popitem()    
  print(f"Longest word in file is '{longest_word[0]}'")
      
      
file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"
find_longest_word(file_name)
      