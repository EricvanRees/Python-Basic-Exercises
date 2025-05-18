"""
Write a Python program to count and display vowels in text.
"""


def count_vowels(astr):
    count_vowels = {}
    for char in astr:
        if char in 'aeiouAEIOU':
            if char in count_vowels.keys():
                count_vowels[char] += 1
            else:
                count_vowels[char] = 1

    return count_vowels


mystr = "Write a Python program to swap commas and dots in a string."
print(count_vowels(mystr))
