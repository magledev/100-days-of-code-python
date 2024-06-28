from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/spanish_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_1000_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_side = current_card["Spanish"]
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=french_side, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_side = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_side, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def known_card():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/spanish_words_to_learn.csv", index=False)
    next_card()

# ---------------------- UI SETUP ---------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 32, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 54, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, border=0, command=next_card)
unknown_button.grid(row=2, column=0)
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, border=0, command=known_card)
known_button.grid(row=2, column=1)

next_card()

window.mainloop()
