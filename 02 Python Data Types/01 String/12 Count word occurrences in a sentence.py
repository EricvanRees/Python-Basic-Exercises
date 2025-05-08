"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

def count_word_occurrences(astr):
  newstr = astr.split(" ")
  count_occ = {}
  for el in newstr:
    if count_occ.get(el):
      count_occ[el] += 1
    else:
      count_occ[el] = 1
      
  return count_occ

mystr = "This is a sentence with a set of repeated words. I said repeated words."
print(count_word_occurrences(mystr))