"""This is the official way to set up the grid. It does not work on my machine :|
That's OK though! That's #learning#"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

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
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}"
                            f"\nPassword: {password} Is it okay to save?")
        if is_ok:
            # I did it this way:
            # try:
            #     with open("json.dump", "r") as myfile:
            #         data = json.load(myfile) #Load data from the json file
            #         data.update(new_data) #Update it with new data
            #     with open("json.dump", "w") as myfile: #Writing the data now.
            #         json.dump(data, myfile, indent=4) #write json
            # except FileNotFoundError:
            #     with open("json.dump", "a") as myfile:
            #         json.dump(new_data, myfile, indent=4) #write json
            #The course does it this way, which is a little cleaner.
            try:
                with open("json.dump", "r") as myfile:
                    data = json.load(myfile) #Load data from the json file
            except FileNotFoundError:
                with open("json.dump", "w") as myfile:
                    json.dump(new_data, myfile, indent=4) #write json
            else:
                data.update(new_data) #Update it with new data
                with open("json.dump", "w") as myfile: #Writing the data now.
                    json.dump(data, myfile, indent=4) #write json
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ------------------------ SEARCH FOR ENTRY --------------------------- #

#My version:
# def search():
#     """Search for a json entry and let you know the password/user via popup.
#     If there's nothing show a popup saying 'no data file found'. """
#     website = website_entry.get()
#     try:
#         with open("json.dump", "r") as myfile:
#             data = json.load(myfile) #Load data from the json file
#             website_data = data[website]
#             retrieved_username = website_data["username"]
#             retrieved_password = website_data["password"]
#             messagebox.showinfo(title=f"{website}", message=f"Username: {retrieved_username}\n Password: {retrieved_password}")
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No data file found.")
#     except KeyError:
#         messagebox.showinfo(title="Empty", message="No details for the website exist in your passwords.")

#The course version:
def search():
    """Search for a json entry and let you know the password/user via popup.
    If there's nothing show a popup saying 'no data file found'. """
    website = website_entry.get()
    try:
        with open("json.dump", "r") as myfile:
            data = json.load(myfile) #Load data from the json file
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            retrieved_username = data[website]["username"]
            retrieved_password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Username: {retrieved_username}\n Password: {retrieved_password}")
        else:
            messagebox.showinfo(title="Empty", message="No details for the website exist in your passwords.")

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
website_entry=Entry(width=21)
username_entry=Entry(width=40)
password_entry=Entry(width=21)

#Buttons
pw_gen_button=Button(text="Generate Password", width=15, command=generate_password)
add_button=Button(text="Add", width=36, command=save)
search_button=Button(text="Search", width=15, command=search)

canvas.grid(column=1,row=0)
website_label.grid(column=0,row=1)
name_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)
website_entry.grid(column=1,row=1)
search_button.grid(column=2,row=1)
username_entry.grid(column=1,row=2, columnspan=2)
username_entry.insert(0, "testemail@example.com")
password_entry.grid(column=1,row=3)
pw_gen_button.grid(column=2,row=3)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop() #Gotta have this here for the program to run at all.