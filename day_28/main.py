from tkinter import *
import math
import time
import datetime
"""Pomodoro!
I will note, tkinter doesn't have a round button. You have to draw it in Canvas or use 
images in canvas to actually have a round button. Which is gross IMO. Seriously. :|
... So we have square buttons. So it goes.
I only have two real additions to this: I disable the start button after starting,
and I used timedelta, though I removed timedelta as what the instructor wanted
became more obvious."""
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK="✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Resets the timer and stops the countdown. Re-enables the start button."""
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    success_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    enable_start_button()
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Calls a 25-minute countdown."""
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="You Better Work", fg=GREEN)
        count_down(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Input the number of seconds. This will count down to 0, and update the checkmarks at the end.
    Disable the start button while the pomodoro is happening.
    Globals: reps, timer"""
    global reps, timer
    disable_start_button()
    count_min = str(math.floor(count/60))
    count_sec = str(count % 60)
    if int(count_sec) < 10:
        count_sec = "0" + count_sec
    # canvas.itemconfig(timer_text, text=str(datetime.timedelta(seconds=count))) The course doesn't want us to use timedelta :(
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        work_sessions = math.floor(reps/2)
        success_label.config(text=work_sessions*CHECKMARK) # Update the checkmarks to show how many reps we've gone through!
        start_timer()

# ------------------ DISABLE/ENABLE START BUTTON ---------------------- #

def disable_start_button():
    start_button["state"]="disabled"

def enable_start_button():
    start_button["state"]="enable"

# ---------------------------- UI SETUP ------------------------------- #
#Create and configure window.
window = Tk()
window.title("Pomodoro")
window.minsize(width=600,height=300)
window.config(padx=100, pady=50, bg=YELLOW) #bg for background color, fg for foreground if needed

#Import and create the image. First make a canvas object:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") #Then make this photoimage to then, after, create an image with this PhotoImage.
canvas.create_image(100,112, image=tomato_img) # x and y values are centering the image.
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

#Make the labels.

timer_label= Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)

success_label=Label(text=CHECKMARK, font=(FONT_NAME, 10, "bold"))
success_label.config(fg=GREEN, bg=YELLOW)

#Make the buttons.
start_button=Button(text="Start", command=start_timer)
start_button.config(fg="black",bg="white",font=("Arial",10,"bold"),highlightthickness=0)
reset_button=Button(text="Reset", command=reset_timer)
reset_button.config(fg="black",bg="white",font=("Arial",10, "bold"),highlightthickness=0)
#Show all the objects onscreen.

timer_label.grid(column=1,row=0) #Show the timer label.
canvas.grid(column=1,row=1) #Show the tomato image onscreen.
start_button.grid(column=0,row=2) #Show the start button.
reset_button.grid(column=2,row=2) #Show the reset button.
success_label.grid(column=1,row=3) #Show the label of checkmarks.

#This ends the program. Without it nothing will show on the screen, haha.
window.mainloop()