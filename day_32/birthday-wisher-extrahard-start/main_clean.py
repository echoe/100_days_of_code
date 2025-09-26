import pandas
import smtplib
import random
import datetime as dt
##################### Extra Hard Starting Project ######################
"""Above: required imports. Below: constants and such.
It looks like the official solution had a dictionary comprehension, but I just matched the month and day with an if line.
Other than that, I think this is pretty clean, especially with pulling all the constants out of the functions!"""

# Constants
SMTP_URL="smtp.gmail.com" #Gmail's SMTP server.
EMAIL="sample_email@gmail.com" # This is a gmail email since it's what the course uses. Fill in whatever.
USERNAME="test_user"
PASSWORD="test_password" # FYI: most email providers require a specific app password for you to send emails for security purposes.
RECIPIENT="someoneelse@example.com"
QUOTES="quotes.txt"
BIRTHDAYS="birthdays.csv"
letter_list=["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

def mock_email(smtp_url,user,password,from_addr,to_addrs,msg):
    """Prints an email and all the things used to send an email. Does not send an email."""
    print(f"You sent an email to {to_addrs} from {from_addr}! It said: \n{msg} \n"
          f"The email was sent with the credentials User: {user} Password: {password} SMTP URL: {smtp_url}")

now = dt.datetime.now() # Get the day so we can use it in this check.
birthdays = pandas.read_csv(BIRTHDAYS) # Get our list of birthdays to also check.
for row in birthdays.iterrows():
    if row[1]['month'] == now.month and row[1]['day'] == now.day: # If the month and day match, the birthday matches
        letter = random.choice(letter_list) # Pick a random letter from the list to send!
        with open(letter) as birthday_letter:
            letter_contents = birthday_letter.read()
        letter_contents = letter_contents.replace("[NAME]",row[1]['name']) # Pull the letter and then replace the placeholder.
        mock_email(SMTP_URL,USERNAME,PASSWORD,EMAIL,RECIPIENT,"Subject:Happy Birthday!\n\n"+letter_contents) # Send using the mock_email function above.