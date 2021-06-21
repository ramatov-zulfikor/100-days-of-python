from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    all_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    all_words = pandas.read_csv("data/french_words.csv")
    to_learn = all_words.to_dict(orient="records")
else:
    to_learn = all_words.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    
    flashcard.itemconfig(card, image=card_front)
    flashcard.itemconfig(title, text="French", fill="black")
    flashcard.itemconfig(word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flashcard.itemconfig(card, image=card_back)
    flashcard.itemconfig(title, text="English", fill="white")
    flashcard.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI
window = Tk()
window.title("Flash Card App")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = flashcard.create_image(400, 263, image=card_front)
title = flashcard.create_text(400, 100, text="", font=("Arial", 30, "italic"))
word = flashcard.create_text(400, 263, text="", font=("Arial", 50, "bold"))
flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

next_card()
window.mainloop()
