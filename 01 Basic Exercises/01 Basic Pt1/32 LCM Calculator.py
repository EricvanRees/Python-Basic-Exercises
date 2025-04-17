"""
Write a Python program to find the least common multiple (LCM) of two positive integers.
"""

def calc_lcm(int1, int2):
  muls1 = []
  muls2 = []

  x = range(0, int1 * 10, int1)
  for n in x:
      n += int1
      muls1.append(n)

  y = range(0, int2 * 10, int2)
  for m in y:
      m += int2
      muls2.append(m)

  print(f"Least Common Multiple of integers {int1} and {int2} is {sorted(list(set(muls1).intersection(muls2)))[0]}")

calc_lcm(4, 5)