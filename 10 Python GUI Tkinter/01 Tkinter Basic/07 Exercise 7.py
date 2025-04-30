"""
Write a Python GUI program that adds labels and buttons to the Tkinter window.
"""

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('New Window')
window.configure(background='#6666ff')

def add_label():
  label = tk.Label(window, text="This is my label")
  label.config(font=("Arial", 25, "bold"))
  # publish label
  label.pack(pady=20)

#buttons
button1 = ttk.Button(window, text='Click Here to Add Label', command=add_label)
button1.pack(pady=20)

window.mainloop()