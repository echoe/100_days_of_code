"""making a tkinter program to convert miles to km.
This looks a little shoddy but I didn't want to use config to change every font etc. ..."""
import tkinter

#make functions first.
def convert_miles_to_km():
    """Convert miles to km. Google says you just multiply it by this number."""
    output_label.config(text=str(1.609344 * float(my_input.get())))

#write out the tkinter things, starting with the window.
my_window = tkinter.Tk()
my_window.title("Mile to Km Converter") # Couldn't pass title in the config options.
my_window.config(padx=20, pady=20) # Try to make this a little spaced out.

#tkinter objects.
my_input = tkinter.Entry(width=7) # I did not know you could just set width like this, that's new :)
miles_label = tkinter.Label(text="Miles")
km_label = tkinter.Label(text="Km")
output_label = tkinter.Label(text="0")
is_equal_label = tkinter.Label(text="is equal to")
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)

# arrange them all on a grid.
my_input.grid(column=1,row=0)
miles_label.grid(column=2,row=0)
is_equal_label.grid(column=0,row=1)
output_label.grid(column=1,row=1)
km_label.grid(column=2,row=1)
calculate_button.grid(column=1,row=2)

# main loop will keep window on screen and listen for the user, to interact with it. This needs to be at the end of the program
my_window.mainloop()