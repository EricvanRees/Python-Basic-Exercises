"""
Write a Python program to reverse words in a string.
"""


def reverse_words(astr):
    newlist = []
    for word in astr.split(" "):
        word = word[::-1]
        newlist.append(word)
    newstr = ' '.join(newlist)
    return newstr


print(reverse_words('This is a string with words.'))
