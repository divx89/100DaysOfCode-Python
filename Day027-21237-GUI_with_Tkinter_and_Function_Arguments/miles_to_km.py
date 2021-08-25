from tkinter import *

window = Tk()
window.title("Miles to Km Converter")

input_entry = Entry(width=10)
input_entry.insert(END, 0)
input_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)
equals_label.config(padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

km_value = Label(text="0")
km_value.grid(column=1, row=1)
km_value.config(padx=5, pady=5)


def calculate():
    miles = float(input_entry.get())
    km = round(1.609 * miles, 3)
    km_value.config(text=f"{km}")


calculator = Button(text="Calculate", command=calculate)
calculator.grid(column=1, row=2)
calculator.config(padx=5, pady=5)

window.mainloop()
