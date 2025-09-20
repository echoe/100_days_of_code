#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
DEFAULT_FILEPATH="C:/Users/youruser/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/"
INVITED_NAMES="Input/Names/invited_names.txt"
PLACEHOLDER_INPUT="Input/Letters/starting_letter.txt"
PLACE_TO_SEND="Output/ReadyToSend"
PLACEHOLDER="[name]" # I added this after watching the walkthrough video. Not necessary ... but why not?
with open(DEFAULT_FILEPATH + PLACEHOLDER_INPUT, "r") as starting_letter:
    start_letter = starting_letter.read()

with open(DEFAULT_FILEPATH + INVITED_NAMES) as names_file:
    for line in names_file.readlines():
        name = line.strip("\n")
        print(start_letter.replace(PLACEHOLDER,name))
        with open(DEFAULT_FILEPATH + PLACE_TO_SEND + "/" + name, "w") as writing_letter:
            writing_letter.write(start_letter.replace("[name]",name))