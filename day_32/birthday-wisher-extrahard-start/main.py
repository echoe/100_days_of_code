import pandas
import smtplib
import random
import datetime as dt
##################### Extra Hard Starting Project ######################
"""Above: required imports. Below: parts of the stuff we walked through earlier in the day.
It looks like the official solution had a dictionary comprehension, but I just matched the month and day with an if line.
Watching the official walkthrough I think this is pretty good, though, since you need to use the rest of the row if you send.
The parts of the puzzle that are listed as things you have to do are left in the codebase for clarity.
I did, perhaps, overuse constants ... but I would rather err that way than the other."""

# Constants
SMTP_URL="smtp.gmail.com" #Gmail's SMTP server.
EMAIL="sample_email@gmail.com" # This is a gmail email since it's what the course uses. Fill in whatever.
USERNAME="test_user"
PASSWORD="test_password" # FYI: most email providers require a specific app password for you to send emails for security purposes.
RECIPIENT="someoneelse@example.com"
QUOTES="quotes.txt"
BIRTHDAYS="birthdays.csv"
letter_list=["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

# 4. Send the letter generated in step 3 to that person's email address.

def send_email(my_smtp_url,my_user,my_password,my_from_addr,my_to_addrs,my_msg):
    """Send an email with the required inputs."""
    with smtplib.SMTP(my_smtp_url) as connection:
        connection.starttls() #adding TLS security to the email.
        connection.login(user=my_user,password=my_password)
        connection.sendmail(from_addr=my_from_addr,to_addrs=my_to_addrs, msg=my_msg)

# let's make a mock email printer so we can pretend that we're sending mail without doing it too!

def mock_email(smtp_url,user,password,from_addr,to_addrs,msg):
    """Prints an email and all the things used to send an email. Does not send an email."""
    print(f"You sent an email to {to_addrs} from {from_addr}! It said: \n{msg} \n"
          f"The email was sent with the credentials User: {user} Password: {password} SMTP URL: {smtp_url}")

# 1. Update the birthdays.csv - I did this within birthdays.csv :)

# 2. Check if today matches a birthday in the birthdays.csv! Pretty simple :)

now = dt.datetime.now()
birthdays = pandas.read_csv(BIRTHDAYS)
for row in birthdays.iterrows():
    # print(row[1]['name'], row[1]['email'], row[1]['year'], row[1]['month'], row[1]['day'])
    if row[1]['month'] == now.month and row[1]['day'] == now.day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(letter_list)
        with open(letter) as birthday_letter:
            letter_contents = birthday_letter.read()
        letter_contents = letter_contents.replace("[NAME]",row[1]['name'])
        mock_email(SMTP_URL,USERNAME,PASSWORD,row[1]['email'],RECIPIENT,"Subject:Happy Birthday!\n\n"+letter_contents)