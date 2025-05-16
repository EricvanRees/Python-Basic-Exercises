"""
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""


def count_chars(astr, chars_to_count):
    counts = {}
    for letter in astr:
        if letter in chars_to_count:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts


mystr = 'thequickbrownfoxjumpsoverthelazydog'
chars = 'oeuhrt'
print(count_chars(mystr, chars))
