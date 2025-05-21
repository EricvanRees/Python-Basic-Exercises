"""
Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".
"""


def return_common_chars(string1, string2):
    string1_sort = set(''.join(sorted(string1)))
    string2_sort = set(''.join(sorted(string2)))
    intersection = string1_sort.intersection(string2_sort)
    if len(intersection) > 1:
        print(f"common chars are {intersection}")
    else:
        print("There are no common characters.")


return_common_chars("aaazziijjnnbb", "zyxoabee")
return_common_chars("abc", "zyx")
