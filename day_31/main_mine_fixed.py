from tkinter import *
import pandas
from random import choice

# Constants.
LANGUAGEFONT=("Arial",40,"italic")
MAINFONT=("Arial",60,"bold")
BACKGROUND_COLOR = "#B1DDC6"
CSV_FILE="data/french_words.csv"
LEARNING_FILE="data/words_to_learn.csv"

# Globals.
# Check for words_to_learn.csv and load it if it exists. If not, get the default file #
try:
    card_list = pandas.read_csv(LEARNING_FILE).to_dict(orient="records")
except FileNotFoundError:
    card_list = pandas.read_csv(CSV_FILE).to_dict(orient="records")
card_list_choice = None
pending_flip = None

# Step 2, handling the cards #

def draw_new_card():
    """Draws a new card."""
    global pending_flip, card_list_choice
    window.after_cancel(pending_flip) #Cancel a flip if it was pending.
    card_list_choice = choice(card_list) # Make a card choice.
    flashcard.itemconfig(flashcard_img, image = card_front_img) #Update the card: starting with image to card_front.
    flashcard.itemconfig(title_text,text="French")#Update title text.
    flashcard.itemconfig(word_text,text=card_list_choice['French'])#Update main text.
    pending_flip = window.after(3000, flip_card) #Start the flip process.

# Step 4, writing the updated word list to the csv.

def update_word_list():
    """Removes a word from the list, updates the csv, then draws a new card."""
    global card_list, card_list_choice
    pd_card_list = pandas.DataFrame.from_records(card_list).drop(card_list.index(card_list_choice)) #pull in the current index, then drop the current card_list_choice
    pd_card_list.to_csv(LEARNING_FILE)
    card_list = pd_card_list.to_dict(orient="records")
    draw_new_card()

# Step 3, flip the card if you don't know what it is #

def flip_card():
    """Flips the card over, showing you the other side. That's it. You don't need to do the other stuff!!"""
    flashcard.itemconfig(flashcard_img, image = card_back_img)
    flashcard.itemconfig(title_text,text="English")#Update title text.
    flashcard.itemconfig(word_text,text=card_list_choice['English'])#Update main text.

# Step 1, the UI #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR) #Padding, as required

#Import and create the images, including text.
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
flashcard_img = flashcard.create_image(400,263,image=card_front_img) # x and y values are centering the image.
title_text = flashcard.create_text(400,150,text="Title",font=LANGUAGEFONT) # Say a word.
word_text = flashcard.create_text(400,263,text="word",font=MAINFONT) # Say a word.

#And now, buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=update_word_list) # x and y values are centering the image.

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=draw_new_card) # x and y values are centering the image.

flashcard.grid(row=0,column=1,columnspan=2)
right_button.grid(row=1,column=1)
wrong_button.grid(row=1,column=2)

#Set pending flip before drawing a new card so we don't have an error.
pending_flip = window.after(3000, flip_card) #Start the flip process.
draw_new_card() # Draw a card immediately so you don't have to deal with the 'no cards' loophole.

window.mainloop() #Gotta have this here for the program to show anything.