"""nato alphabet 'program'! I did not use any of the starter code, but I did copy the csv over."""
import pandas
NATO_ALPHABET_FILE = "nato_phonetic_alphabet.csv"

df = pandas.read_csv(NATO_ALPHABET_FILE)
#TODO: - Create a dictionary in this format: key[letter]: value[code]
# ... This took me a minute. Walking through it:
# df.iterrows() here gives you [index], [letter:nato result]. So you pull row[0] and row [1] and it gets you there.
# I also did row[1][0]:row[1] which also works (T for Tango etc) but that's more of a fluke of what the fields are than anything.
# natodict = {row[0]:row[1] for (index, row) in df.iterrows()}
# The course wants you to call it by name though, which does make more sense:
natodict = {row.letter:row.code for (index, row) in df.iterrows()}
#TODO 2: Create a list of the phonetic code words from a word the user inputs. 
# I tried to convert into a dictionary when I needed to convert into a list for like 30 minutes here :| I was so tired today.
my_input = input("Type a word to convert into the nato phonetic alphabet!: ").upper() # We grab a word.
# This is how to do it via for loop.
# myoutput=[]
# for letter in list(my_input):
#     myoutput.append(natodict[letter.upper()])
# This is doing it via dictionary comprehension, which doesn't give you the output in the proper order because it gives you a dictionary, oops.
# output = {natodict[letter.upper()] for letter in list(input)}
# Doing it correctly via list comprehension.
print([natodict[letter] for letter in list(my_input)])