# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Room 12")
# Set geometry (widthxheight)
root.geometry('350x200')

# all widgets will be here
# adding a label to the root window
lbl = Label(root, text = "Hello world!")
lbl.grid()

# function to display text when button is clicked
def clicked():
    lbl.configure(text="You shouldn't click it.")

# button widget with red color text inside
btn = Button(root, text = "Don't click me",
             fg = "red", command = clicked)
# set Button grid
btn.grid(column = 1, row = 1)

# Execute Tkinter
root.mainloop()
