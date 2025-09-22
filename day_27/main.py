import tkinter
from tkinter import Button, Entry
""" It's pronounced 'T-K-Inter', thanks so much."""
ARIAL=("Arial", 24, "bold")

window = tkinter.Tk()
window.title("Title")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #add padding between things. you can also do this with a specific widget, using .config

#Label
tkinter_label = tkinter.Label(text="This is a label", font=ARIAL)
#First, create a component. Then, specify how the component is laid out on the screen, and /then/ it shows up.
# tkinter_label.pack(side="left") #Places the label into the screen, automatically centered but you can pick options if you want.
# [and starts at the top of the screen, automatically going down as more labels are added].
# There are options to move it left or right etc. etc., covered in the documentation.
# tkinter_label.place(x=0, y=0) #Place a label at an exact spot in the window
tkinter_label.grid(column=0, row=0) # [places it in a grid relative to other components]
tkinter_label_2 = tkinter.Label(text="also")
# tkinter_label_2.pack()
tkinter_label_2.grid(column=1,row=0) #You can't use pack and grid in the same GUI

tkinter_label["text"] = "UPDATING LABEL NOW"
tkinter_label.config(text="NVM UPDATE AGAIN")

def button_clicked():
    print("you did it!")
    tkinter_label["text"]=input.get()

button = Button(text = "click me", command=button_clicked)
# button.pack()
button.grid(column=2,row=0)

button2 = Button(text = "also click me", command=button_clicked)
# button.pack()
button2.grid(column=1,row=1)

input = Entry(width=10) #This is an entry thing.
# input.pack()
input.grid(column=3,row=2)

window.mainloop() # main loop will keep window on screen and listen for the user, to interact with it. This needs to be at the end of the program