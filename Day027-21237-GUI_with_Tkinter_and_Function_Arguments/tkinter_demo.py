from tkinter import *
import random

# Create a window
window = Tk()

# Give the window a title
window.title("First GUI Program")

# Specify the minimum size of the window.
# It will resize according to its components.
# This is the starting size
window.minsize(width=500, height=300)


# Creating a function that has multiple positional arguments in one keyword
# VarArgs
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# Creating a function that requires named arguments
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


greet_me(total=add(5, 6, 7, 8, 9), new_total=add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Creating components
# ###################
# Create a label in the window
my_label = Label(text=f"{add(1, 2, 3, 4)}", font=("Arial", 12, "normal"))
# Place the label in the window
my_label.pack(side="top")


# Creating buttons
def button_clicked():
    num_of_numbers = random.randint(2, 5)
    *numbers, = [random.randint(1, 100) for number in range(num_of_numbers)]
    my_label["text"] = f"{input_entry.get()}, The sum of {numbers} is {add(*numbers)}"


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Input/Entry
input_entry = Entry(width=20)
input_entry.insert(END, string="Something")
input_entry.pack()

# Multi-line Text Entry - Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox (a counter)
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale (used to navigate in a page)
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check-boxes
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio Buttons
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List Box
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
