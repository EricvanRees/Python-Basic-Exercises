"""
Write a Python program that accepts some words and counts the number of distinct words. Print the number of distinct words and the number of occurrences of each distinct word according to their appearance.

Input number of words: 5
Input the words:
Red
Green
Blue
Black
White
5
1 1 1 1 1
"""
from collections import OrderedDict, Counter


def count_input(myinputstr):
    mylist = myinputstr.split(" ")
    word_tot = len(mylist)
    counterobj = Counter(mylist)
    list_counterobj = list(counterobj.values())
    myordereddict = OrderedDict.fromkeys(mylist)
    res = list(myordereddict)
    print(f"Input number of words: {word_tot}")
    for key in res:
        print(key)
    print(len(res))
    print(*list_counterobj, sep=',')


count_input("Red Green Blue Black White")
