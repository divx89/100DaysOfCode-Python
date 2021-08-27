from tkinter import *
from tkinter import messagebox
from password_generator import *
import pyperclip


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

    # Ask user if it is ok to proceed
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered:\n"
                                           f"Email: {username}\n"
                                           f"Password: {password}\n"
                                           f"Is it ok to save?")

    # If user is ok to proceed, open the file,
    # write the data, and then clear the fields
    if is_ok:
        with open(file="data.txt", mode="a") as fileHandle:
            fileHandle.write(f"{website} | {username} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


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
#               Entries
# -----------------------------------------
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

username_entry = Entry(width=55)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
username_entry.insert(END, "james.spader@randomperson.get")

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, sticky=W)
# -----------------------------------------

# -----------------------------------------
#               Buttons
# -----------------------------------------
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky=E)

add_button = Button(text="Add", command=save_password, width=46)
add_button.grid(column=1, row=4, columnspan=2)
# -----------------------------------------

window.mainloop()
