"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""

def gen_dict(n):
  mylist = []
  mylist_sq = []
  for i in range(1, n):
    mylist.append(i)

  for j in range(1, n + 1):
    mylist_sq.append(j * j)
    
  res = {key: value for key, value in zip(mylist, mylist_sq)}
  return res

print(gen_dict(4))