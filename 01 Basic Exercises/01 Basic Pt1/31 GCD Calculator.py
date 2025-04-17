"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def calc_gcd(a_num, another_num):
  if a_num > 1 and another_num > 1:
    div1 = []
    div2 = []
    x = range(1, a_num + 1)
    for n in x:
      if a_num % n == 0:
        div1.append(n)

    y = range(1, another_num + 1)
    for m in y:
      if another_num % m == 0:
        div2.append(m)

  else:
    return False
  
  return f"Greatest common divisor of integers {a_num} and {another_num} is {list(set(div1).intersection(div2))[-1]}"

print(calc_gcd(10, 56))