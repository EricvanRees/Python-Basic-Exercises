"""
Write a Python program to count the frequency of words in a file.
"""

file_name = r"C:\\Users\\mipc\\Downloads\\test.txt"

def count_freq(my_file):
  word_count = {}
  with open(my_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      for word in line.split():
        if word_count.get(word) == None:
          word_count[word] = 0
        else:
          word_count[word] += 1
      
  item_count = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1])}
  return item_count

print(count_freq(file_name))
          