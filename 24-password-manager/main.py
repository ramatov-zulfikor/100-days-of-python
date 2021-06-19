from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json


def generate_password():
    """ Generate password """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(8)]
    password_numbers = [choice(numbers) for _ in range(2)]
    password_symbols = [choice(symbols) for _ in range(2)]

    password = password_letters + password_numbers + password_symbols

    shuffle(password)
    password_input.insert(0, ''.join(password))
    pyperclip.copy(password_input.get())


def save_password():
    """ Save password to data.json """
    user_website = website_input.get().lower()
    user_email = email_input.get()
    user_password = password_input.get()

    user_data = {
        user_website: {
            "email": user_email,
            "password": user_password
        }
    }

    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(user_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(user_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search_password():
    """ Search password from data.json """
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            result = data[website.lower()]
            messagebox.showinfo(title=website, message=f"Email: {result['email']}\n Password: {result['password']}")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for the website exists")


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=49)
email_input.grid(row=2, column=1, columnspan=2)
# Here you can uncomment line under and set your email by default
email_input.insert(0, "example@email.com")

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
