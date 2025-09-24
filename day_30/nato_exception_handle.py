"""nato alphabet 'program'! I did not use any of the starter code, but I did copy the csv over."""
import pandas
NATO_ALPHABET_FILE = "nato_phonetic_alphabet.csv"

df = pandas.read_csv(NATO_ALPHABET_FILE)
natodict = {row.letter:row.code for (index, row) in df.iterrows()}

# I did this to fix this code.
# waiting_for_word = True
# while waiting_for_word:
#     try:
#         my_input = input("Type a word to convert into the nato phonetic alphabet!: ").upper() # We grab a word.
#         print([natodict[letter] for letter in list(my_input)])
#         waiting_for_word = False
#     except KeyError:
#         print("Sorry, you can only type letters in the alphabet, please.")

#Angela does it this way, which does seem nice and clean:
def generate_phonetic():
    try:
        my_input = input("Type a word to convert into the nato phonetic alphabet!: ").upper() # We grab a word.
    except KeyError:
        print("Sorry, you can only type letters in the alphabet, please.")
        generate_phonetic()
    else:
        print([natodict[letter] for letter in list(my_input)])

generate_phonetic()