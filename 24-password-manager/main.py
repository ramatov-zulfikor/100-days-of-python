from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip


def generate():
    """Generate password"""
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


def save():
    """Save password to data.txt"""
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()

    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: "
                                                                   f"\nEmail: {user_email} "
                                                                   f"\nPassword: {user_password} "
                                                                   f"\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{user_website} | {user_email} | {user_password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


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
website_input = Entry(width=49)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=49)
email_input.grid(row=2, column=1, columnspan=2)
# Here you can uncomment line under and set your email by default
# email_input.insert(0, "example@email.com")

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
