"""
Write a Python GUI program that adds labels and buttons to the Tkinter window.
"""

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('New Window')
window.configure(background='#6666ff')

def add_btn():
  y = 5
  new_button = ttk.Button(window, text="New Button")
  new_button.pack(pady=y)
  
#buttons
button1 = ttk.Button(window, text='Click Here to Add Button', command=add_btn)
button1.pack(pady=20)

window.mainloop()