"""
Write a Python program that customizes the appearance of labels and buttons (e.g., fonts, colors) using Tkinter.
"""

import tkinter as tk
from tkinter import ttk

# create window
window = tk.Tk()
window.geometry('800x600')
window.title('My new window')
window.configure(background="#040f75")

# create a style
styles = ttk.Style()
styles.theme_use('clam')
styles.configure(window, background="#FFFFFF",
                 foreground='black', fieldbackground='white')
styles.configure('TButton', background="#3395f0")
styles.map('TButton', background=[('active', "#18e7eb")])


def show():
    text = textbox.get()
    print(f'text provided: {text}')
    label['text'] = text


# text box
textbox = ttk.Entry(window, font=('Tahoma', 14))
textbox.pack(pady=25)

# add button
button = ttk.Button(window, text='Send', command=show)
button.pack(pady=20)

# add label
label = ttk.Label(window, text='Initial value')
label.config(font=("Arial", 16, "italic"))
label.pack(pady=20)

window.mainloop()
