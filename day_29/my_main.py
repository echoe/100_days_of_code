"""Password managers are great, but I don't know if saving passwords locally on one single device is a great idea.
Anyways this day's project is a password manager. I wrote this by myself before watching the lesson.
I used place to get the most accurate placement. I know it looks a little worse but that's ok(tm)!
I also redid the pw_gen to use list stuff per day 26, so I could remember that more ...
This feels like a review day. Which isn't terrible :D"""
#Imports
from tkinter import *
import tkinter.messagebox as messagebox
import random, csv, string

#Variables
PW_STORE="passwords.csv"
FONT = ("Arial",13) # Feel free to adjust to taste.

#Set up the canvas and stuff
window = Tk()
window.minsize(width=500,height=500)

#functions to use to make buttons do things
def pw_gen():
    """generates a password and replaces the password input contents with said password"""
    random_pass=''.join([random.choice(string.printable) for i in range(1,10)])
    # Note that you can get tab randomly from this
    password_entry.delete(0,'end')
    password_entry.insert(0,random_pass)
    # And let's put it into the clipboard, as the example does.
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())

def add_pw_to_store():
    """adds password to our password store. If there is no file at PW_STORE, create the file.
    Commented to place the input in the way the example code does.
    Spaced as the example shows.
    Using csv because I can't be assed to import pandas for this. For /this/? Come on now."""
    # try:
    #     with open(PW_STORE) as csvfile:
    #         pass
    # except FileNotFoundError:
    #     with open(PW_STORE, 'a') as csvfile:
    #         write_passwords = csv.writer(csvfile, delimiter=" | ")
    #         write_passwords.writerow(["Website","Username","Password"])
    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Error",message="You need to fill out all the boxes! At least one is empty")
    else:
        with open(PW_STORE, 'a') as csvfile:
            write_passwords = csv.writer(csvfile, delimiter="|")
            write_passwords.writerow([website_entry.get()+" "," " + username_entry.get()+" "," " +password_entry.get()])

#Import and create the lock image. I found this on google.
canvas = Canvas(width=320, height=320, highlightthickness=0)
lock_img = PhotoImage(file="lock.png") #Then make this photoimage to then, after, create an image with this PhotoImage.
canvas.create_image(160,160, image=lock_img) # x and y values are centering the image.

#Labels

website_label=Label(text="Website:",font=FONT)
name_label=Label(text="Email/Username:",font=FONT)
password_label=Label(text="Password",font=FONT)

#Inputs
website_entry=Entry(width=40)
username_entry=Entry(width=40)
password_entry=Entry(width=20)

#Buttons
pw_gen_button=Button(text="Generate Password", command=pw_gen)
add_button=Button(text="Add",command=add_pw_to_store, width=35)

#Set up the grid. This is commented out so we can use place instead.
#I added columnspan in these comments specifically just to look at it as I go through day 29, haha.

# canvas.grid(column=1,row=0)
# website_label.grid(column=0,row=1)
# name_label.grid(column=0,row=2)
# password_label.grid(column=0,row=3)
# website_entry.grid(column=1,row=1, columnspan=2)
# username_entry.grid(column=1,row=2, columnspan=2)
# password_entry.grid(column=1,row=3)
# pw_gen_button.grid(column=2,row=3)
# add_button.grid(column=1,row=4)

# It's place time baybeeee. Set up the places.

canvas.place(x=100, y=50)
website_label.place(x=10, y=380)
name_label.place(x=10, y=410)
password_label.place(x=10, y=440)
website_entry.place(x=140, y=380)
username_entry.place(x=140, y=410)
password_entry.place(x=140, y=440)
pw_gen_button.place(x=280, y=440)
add_button.place(x=140, y=470)

#keep the program open
window.mainloop()