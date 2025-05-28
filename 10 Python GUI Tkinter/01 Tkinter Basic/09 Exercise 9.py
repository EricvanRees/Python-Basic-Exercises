"""
Write a Python program that displays messages in a messagebox using Tkinter.
"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('600x400')
window.title('New Window')
window.configure(background='#6666ff')


question = messagebox.askyesno(title="question", message="Show message?")
if (question == True):
    messagebox.showinfo("showinfo", "Have a great day!")
else:
    messagebox.showwarning("showwarning", "Are you sure?")

window.mainloop()
