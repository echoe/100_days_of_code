from tkinter import *
import pandas
import random

# Constants.
LANGUAGEFONT=("Arial",40,"italic")
MAINFONT=("Arial",60,"bold")
BACKGROUND_COLOR = "#B1DDC6"
CSV_FILE="data/french_words.csv"
LEARNING_FILE="data/words_to_learn.csv"

try:
    card_list = pandas.read_csv(CSV_FILE)
except FileNotFoundError:
    card_list = pandas.read_csv(LEARNING_FILE)
to_learn = card_list.to_dict(orient="records")
current_card = {}

# Step 2, handling the cards #

def next_card():
    """Draws a new card and updates words_to_learn.csv."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flashcard.itemconfig(flashcard_img, image = card_front_img)
    flashcard.itemconfig(title_text, text="French", fill="black")
    flashcard.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    """Remove the current card from the list and save the updated CSV to the CSV_FILE location."""
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv(LEARNING_FILE, index=False)
    next_card()

def flip_card():
    """Flips the card over, showing you the other side."""
    flashcard.itemconfig(title_text,text="English", fill="white")
    flashcard.itemconfig(word_text,text=current_card["English"], fill="white")
    flashcard.itemconfig(flashcard_img, image = card_back_img)

# Step 1, the UI #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR) #Padding, as required

flip_timer = window.after(3000, func=flip_card)

#Import and create the images, including text.
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
flashcard_img = flashcard.create_image(400,263,image=card_front_img) # x and y values are centering the image.
title_text = flashcard.create_text(400,150,text="Title",font=LANGUAGEFONT) # Say a word.
word_text = flashcard.create_text(400,263,text="word",font=MAINFONT) # Say a word.

#And now, buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=is_known) # x and y values are centering the image.
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card) # x and y values are centering the image.

#Grid!
flashcard.grid(row=0,column=1,columnspan=2)
right_button.grid(row=1,column=1)
wrong_button.grid(row=1,column=2)

next_card()

window.mainloop() #Gotta have this here for the program to show anything.