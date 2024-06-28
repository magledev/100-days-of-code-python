import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

FONT_NAME = "Roboto"
WHITE = "white"
BLACK = "black"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", '"', "£", "$", "%", "^", "&", "*", "(", ")"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text,
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(
            title="Incomplete Fields", message="Please complete all fields!"
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------- FIND PASSWORD ----------------------------- #


def find_password():
    website_text = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found.")
    else:
        if website_text in data:
            email = data[website_text]["email"]
            password = data[website_text]["password"]
            messagebox.showinfo(
                title=website_text, message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"Entry for {website_text} not found."
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
my_pass_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=26)
# website_entry.insert(END, string="enter website url...")
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.insert(0, string="<email_address>")
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.focus()

password_entry = Entry(width=26)
# password_entry.insert(END, string="enter password...")
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate_pass_button = Button(
    text="Generate Password",
    command=generate_password,
    width=14,
    bg=WHITE,
    font=(FONT_NAME, 12),
)
generate_pass_button.grid(column=2, row=3)

add_button = Button(
    text="Add", command=add_password, width=38, bg=WHITE, font=(FONT_NAME, 12)
)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(
    text="Search", command=find_password, width=14, bg=WHITE, font=(FONT_NAME, 12)
)
search_button.grid(column=2, row=1)

window.mainloop()
