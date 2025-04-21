"""
Write a Python program to find the available built-in modules.
"""

import subprocess
import sys

def pip_list():
    args = [sys.executable, "-m", "pip", "list"]
    p = subprocess.run(args, check=True, capture_output=True)
    return p.stdout.decode()

print(pip_list())