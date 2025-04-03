"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

def vowel_test(any_letter):
  if any_letter in "aeiou":
    return "letter is vowel"
  else:
    return "letter is not a vowel"
  
print(vowel_test("a"))
print(vowel_test("b"))
print(vowel_test("c"))
print(vowel_test("d"))
print(vowel_test("e"))