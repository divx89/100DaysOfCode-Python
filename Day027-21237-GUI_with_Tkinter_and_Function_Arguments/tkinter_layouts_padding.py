from tkinter import *
import random

# Create a window
window = Tk()

# Give the window a title
window.title("First GUI Program")

# Specify the minimum size of the window.
# It will resize according to its components.
# This is the starting size
# window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
my_label = Label(text=f"Something 01", font=("Arial", 12, "normal"))
# Place the label in the window
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


# Creating buttons
def button_clicked():
    my_label.config(text=input_entry.get())


button = Button(text="Click Me", command=button_clicked)
# button.place(x=200, y=0)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

new_button = Button(text="Random New Button")
new_button.grid(column=2, row=0)
new_button.config(padx=20, pady=20)

# Input/Entry
input_entry = Entry(width=20)
input_entry.insert(END, string="Something")
# input_entry.place(x=0, y=50)
input_entry.grid(column=3, row=2, ipadx=20, ipady=20)


window.mainloop()
