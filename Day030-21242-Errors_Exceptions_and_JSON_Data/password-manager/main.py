from tkinter import *
from tkinter import messagebox
from password_generator import *
import pyperclip
import json


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_entry.get().strip()
    empty_fields = website == ""
    if empty_fields:
        # In case of empty fields, we show a message and return
        messagebox.showinfo(title="Oops!", message="The website field cannot be empty for a search!")
        return
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Data Not Found", message=f"Data not found for the website {website}")
    else:
        if website in data:
            info = data[website]
            messagebox.showinfo(title=f"{website}", message=f"Email: {info['email']}\nPassword: {info['password']}")
        else:
            messagebox.showinfo(title="Data Not Found", message=f"Data not found for the website {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Remove any existing entry in the field
    password_entry.delete(0, END)
    # Generate the password
    generated_pwd = gen_pwd()
    # Put the password in the field
    password_entry.insert(END, generated_pwd)
    # Copy the password to the clipboard
    pyperclip.copy(generated_pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Extract the values
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Check if any of the fields are empty
    empty_fields = website == "" or username == "" or password == ""
    if empty_fields:
        # In case of empty fields, we show a message and return
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
        return

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    try:
        with open(file="data.json", mode="r") as fileHandle:
            # Read the data
            data = json.load(fileHandle)
            # Update the data
            data.update(new_data)
    except FileNotFoundError:
        # Data still has to be written to the file
        # So, the brand new data becomes the data. No updating.
        data = new_data
    finally:
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

    # Open the file in write mode. It gets created if it doesn't exist.
    # Write the updated/new data to the file
    with open(file="data.json", mode="w") as fileHandle:
        json.dump(data, fileHandle, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# -----------------------------------------
#               Labels
# -----------------------------------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky=E)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)
# -----------------------------------------

# -----------------------------------------
#       Entries & Related Buttons
# -----------------------------------------
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=1, sticky=W)
website_entry.focus()

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1, sticky=E)

username_entry = Entry(width=55)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
username_entry.insert(END, "james.spader@randomperson.get")

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, sticky=W)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky=E)
# -----------------------------------------

# -----------------------------------------
#          Independent Buttons
# -----------------------------------------
add_button = Button(text="Add", command=save_password, width=46)
add_button.grid(column=1, row=4, columnspan=2)
# -----------------------------------------

window.mainloop()
