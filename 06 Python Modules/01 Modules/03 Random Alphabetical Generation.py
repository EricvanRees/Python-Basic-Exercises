"""
Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
"""
import random

def generate_random_char():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return random.choice(alphabet)

def generate_random_str_random_length():
  alp_str = ""
  i = 0
  while i < random.randint(5, 20):
    alp_str += generate_random_char()
    i += 1
  
  return alp_str

def generate_random_str_fixed():
  alp_str = ""
  i = 0
  while i < 10:
    alp_str += generate_random_char()
    i += 1
  
  return alp_str

print(generate_random_str_random_length())
print(generate_random_str_fixed())