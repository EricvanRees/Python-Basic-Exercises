"""
Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.

Sample Output:
1
3
5
7
9
Access first three items individually
1
3
5
"""
import array

myarr = array.array('l', [1,3,5,7,9])
mylist = myarr.tolist()
print(mylist[0], mylist[1], mylist[2])