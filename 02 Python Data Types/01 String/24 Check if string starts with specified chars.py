"""
Write a Python program to check whether a string starts with specified characters.
"""


def starts_with(astr, achar):
    if astr.startswith(achar):
        return True
    else:
        return False


print(starts_with("abc", "a"))
print(starts_with("Abracadabra", "A"))
print(starts_with("DEF", "d"))
print(starts_with("ABBA", "z"))
