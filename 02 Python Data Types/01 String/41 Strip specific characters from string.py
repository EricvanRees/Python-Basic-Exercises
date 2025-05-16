"""
Write a Python program to strip a set of characters from a string.
"""

mystr = 'thequickbrownfox'


def strip_chars(astr, chars_to_strip):
    trans_table = str.maketrans('aeiou', '@@@@@')
    newstr = astr.translate(trans_table)
    return newstr


print(strip_chars(mystr, 'aeo'))
