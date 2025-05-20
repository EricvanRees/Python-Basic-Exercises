"""
Write a Python program to capitalize the first and last letters of each word in a given string.
"""


def capitalize_words(astr):
    new_list = []
    for word in astr.split(" "):
        new_word = word[0].upper() + word[1: -1] + word[-1].upper()
        new_list.append(new_word)

    newstr = ' '.join(new_list)
    return newstr


print(capitalize_words("welcome to w3resource"))
