"""
Write a Python GUI program that creates a window with a specific background color using Tkinter.
"""

import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('New Window')
window.configure(background="#4f4974")

window.mainloop()
