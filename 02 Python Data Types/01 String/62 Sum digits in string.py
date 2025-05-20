"""
Write a Python program to compute the sum of the digits in a given string.
"""


def sum_digits(astr):
    mylist = []
    for char in astr:
        if char.isdigit():
            mylist.append(int(char))

    return sum(mylist)


print(sum_digits("w3re1ou1c1"))
