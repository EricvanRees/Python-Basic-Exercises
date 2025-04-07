"""
Write a Python program to get the current username.
"""

import os

def get_username_os():
  os.getenv("USERNAME")
  
  
username = get_username_os()
print(f"Current username: {username}")
  
  