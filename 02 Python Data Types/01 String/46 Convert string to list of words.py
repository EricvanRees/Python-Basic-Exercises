"""
Write a Python program to convert a given string into a list of words.
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
"""


def list_of_words(astr):
    mylist = astr.split(" ")
    return mylist


print(list_of_words("The quick brown fox jumps over the lazy dog."))
