"""
Write a Python program that displays messages in a messagebox using Tkinter.
"""

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('New Window')
window.configure(background='#4d4dff')

def show():
  text = textbox.get()
  label['text'] = text

# textbox
textbox = ttk.Entry(window, font=('Tahoma', 15))
textbox.pack(pady=20)

# add a button
button = ttk.Button(window, text='Send', command=show)
button.pack(pady=20)

# add a label
label = ttk.Label(window, text='Initial value')
label.pack(pady=20)

window.mainloop()