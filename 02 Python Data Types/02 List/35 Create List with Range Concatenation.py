"""
Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

def create_list(alist, n):
  blist =  []
  newlist = []
  for i in range(1, n + 1):
    blist.append(i)
  
  for number in blist:
    for letter in alist:
      newlist.append((str(number) + letter))
  
  return newlist

print(create_list(['p', 'q'], 5))