"""
Write a Python GUI program to add an image (e.g., a logo) to a Tkinter window.
"""
import tkinter as tk
from tkinter import PhotoImage

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load the image
image = PhotoImage(file="C:\\Users\\mipc\\Downloads\\ESA May 2025 800x400.png")

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()
