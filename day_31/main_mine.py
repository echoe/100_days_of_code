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
    """Draws a new card and updates words_to_learn.csv."""
    global card_list, card_list_choice, title_text, word_text, pending_flip
    flashcard.itemconfig(flashcard_img, image = card_front_img)
    if pending_flip:
        flashcard.after_cancel(pending_flip)
    flashcard.delete(title_text)
    flashcard.delete(word_text)
    title_text = flashcard.create_text(400,150,text="French",font=LANGUAGEFONT) # Say a word.
    card_list_choice = choice(card_list)
    card_index = card_list.index(card_list_choice)
    word_text = flashcard.create_text(400,263,text=card_list_choice['French'],font=MAINFONT) # Say a word.
    update_words(card_index)
    pending_flip = flashcard.after(3000, flip_card)

def draw_new_card_miss():
    """Draws a new card."""
    global card_list, card_list_choice, title_text, word_text, misses
    flashcard.after_cancel(flip_card)
    flashcard.delete(title_text)
    flashcard.delete(word_text)
    title_text = flashcard.create_text(400,150,text="French",font=LANGUAGEFONT) # Say a word.
    card_list_choice = choice(card_list)
    card_index = card_list.index(card_list_choice)
    update_words(card_index)
    word_text = flashcard.create_text(400,263,text=card_list_choice['French'],font=MAINFONT) # Say a word.
    flashcard.after(3000, flip_card)

def update_words(index):
    """Updates words_to_list.csv, removing the card that was passed in."""
    global card_list
    pd_card_list = pandas.DataFrame.from_records(card_list).drop(index)
    pd_card_list.to_csv(LEARNING_FILE)
    card_list = pd_card_list.to_dict(orient="records")
    # print(df)


# Step 3, flip the card if you don't know what it is #

def flip_card():
    """Flips the card over, showing you the other side."""
    global title_text, card_list, card_list_choice, word_text
    language = flashcard.itemcget(title_text, 'text')
    flashcard.delete(title_text)
    flashcard.delete(word_text)
    flashcard.itemconfig(flashcard_img, image = card_back_img)
    if language == "French":
        title_text = flashcard.create_text(400,150,text="English",font=LANGUAGEFONT)
        word_text = flashcard.create_text(400,263,text=card_list_choice['English'],font=MAINFONT)
    elif language == "English":
        title_text = flashcard.create_text(400,150,text="French",font=LANGUAGEFONT)
        word_text = flashcard.create_text(400,263,text=card_list_choice['French'],font=MAINFONT)
    else: #If it's not French or English just show the default Title and word.
        title_text = flashcard.create_text(400,150,text="Title",font=LANGUAGEFONT)
        word_text = flashcard.create_text(400,263,text="word",font=MAINFONT)

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
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=draw_new_card) # x and y values are centering the image.

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=draw_new_card_miss) # x and y values are centering the image.

flashcard.grid(row=0,column=1,columnspan=2)
right_button.grid(row=1,column=1)
wrong_button.grid(row=1,column=2)

window.mainloop() #Gotta have this here for the program to show anything.