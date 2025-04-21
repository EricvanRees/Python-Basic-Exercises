"""
Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
"""
import random

def generate_random_char():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return random.choice(alphabet)

i = 0
while i < 10:
  print(generate_random_char())
  i += 1

