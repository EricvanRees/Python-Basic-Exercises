"""
Write a Python program that creates a list of words and use the filter function to extract words that contain more than five letters.
"""

import random


def filter_words_from_list():
    mystr = "abcdefghijklmnopqrstuvwxyz"
    mylist = []
    for a in range(15):
        myword = ''
        for i in range(1, random.randint(2, 15)):
            myword += mystr[random.randint(0, len(mystr) - 1)]
        mylist.append(myword)

    return mylist


def myfunc(x):
    if len(x) > 5:
        return True
    else:
        return False


words_longer_than_five = filter(myfunc, filter_words_from_list())
for word in words_longer_than_five:
    print(word)
