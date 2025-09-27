"""Call up some APIs
I refuse to do kanye west quotes and wanted to practice tkinter, so I downloaded and converted a bunch of stuff and found a 
different API endpoint to make this with. I found some free pictures and wrote my own tkinter code as well.
this isn't perfect but hey, it works well enough, haha.
please only run it a little bit thank you"""
import requests
from tkinter import *
QUOTES_ENDPOINT="https://zenquotes.io/api/random/"
QUOTE_IMAGE="quote_bg_image.png"
BUTTON_IMAGE="button.png"

def retrieve_quote():
    """Grab a quote and put it into the GUI."""
    json_data = [{'q': 'I can never decide whether my dreams are the result of my thoughts or my thoughts the result of my dreams.', 
    'a': 'D. H. Lawrence'}]
    # The above is sample data. Please don't run the requests part too much, save zenquotes.io's bandwidth :)
    response=requests.get(url=QUOTES_ENDPOINT)
    if response.status_code != 200:
        response.raise_for_status()
    json_data = response.json()
    print(json_data)
    canvas.itemconfig(quote_text, text=f"{json_data[0]['q']} from {json_data[0]['a']}")

# set up the GUI
window=Tk()
quote_image=PhotoImage(file=QUOTE_IMAGE)
button_image=PhotoImage(file=BUTTON_IMAGE)
canvas = Canvas(width=700,height=300)

canvas.create_image(350,200,image=quote_image)
quote_text = canvas.create_text(350,200,text="words")
newquote=Button(image=button_image,command=retrieve_quote)

canvas.grid(row=0,column=0)
newquote.grid(row=1,column=0)

window.mainloop() #keep the window alive