"""
Write a Python program to split a string on the last occurrence of the delimiter.
"""


def split_on_last_occurance(astr, delimiter):
    last_pos = astr.rfind(delimiter)
    return f" {astr[0: last_pos]}, {astr[last_pos:]}"


print(split_on_last_occurance("abra-ca-da-bra", "-"))
