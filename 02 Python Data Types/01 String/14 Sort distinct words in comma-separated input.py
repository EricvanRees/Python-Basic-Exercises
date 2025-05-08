"""
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

def print_distinct_words(word_seq):
  return set(sorted(word_seq.split(", ")))

print(print_distinct_words("red, white, black, red, green, black"))