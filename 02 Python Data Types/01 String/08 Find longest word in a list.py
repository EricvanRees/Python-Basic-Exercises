"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

def find_longest_word(alist):
  word_length = {}
  for word in alist:
    word_length[word] = len(word)
  
  return dict(list(word_length.items())[-1:])

mylist = ['abc', 'koffiekan', 'computermeubel', 'autotentoonstelling']
print(find_longest_word(mylist))
    