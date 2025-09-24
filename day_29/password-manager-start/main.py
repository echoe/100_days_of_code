"""This is the official way to set up the grid. It does not work on my machine :|
That's OK though! That's #learning#"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save stuff."""
    # delimiter = " | "
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details engered: \nEmail: {username}"
                            f"\nPassword: {password} Is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as myfile:
                myfile.write(f"{website} | {username} | {password}\n")
                # myfile.write(website_entry.get()+delimiter+username_entry.get()+delimiter+password_entry.get()+"\n") "Not this way :p"
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Import and create the image. First make a canvas object:
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png") #Then make this photoimage to then, after, create an image with this PhotoImage.
canvas.create_image(100,100, image=logo_img) # x and y values are centering the image.

#Labels

website_label=Label(text="Website:")
name_label=Label(text="Email/Username:")
password_label=Label(text="Password")

#Inputs
website_entry=Entry(width=35)
username_entry=Entry(width=35)
password_entry=Entry(width=21)

#Buttons
pw_gen_button=Button(text="Generate Password", width=15, command=generate_password)
add_button=Button(text="Add", width=36, command=save)


canvas.grid(column=1,row=0)
website_label.grid(column=0,row=1)
name_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)
website_entry.grid(column=1,row=1, columnspan=2)
username_entry.grid(column=1,row=2, columnspan=2)
username_entry.insert(0, "testemail@example.com")
password_entry.grid(column=1,row=3)
pw_gen_button.grid(column=2,row=3)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop() #Gotta have this here for the program to run at all.