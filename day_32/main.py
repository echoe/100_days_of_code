"""Send emails! A lot of this will be GMAIL-specific but YMMV, every email provider is different."""
import smtplib
import datetime as dt # gotta love datetime :D
import random # to get a random quote
SMTP_URL="smtp.gmail.com" #Gmail's SMTP server.
EMAIL="sample_email@gmail.com" # This is a gmail email since it's what the course uses. Fill in whatever.
USERNAME="test_user"
PASSWORD="test_password" # FYI: most email providers require a specific app password for you to send emails for security purposes.
RECIPIENT="someoneelse@example.com"
QUOTES="quotes.txt"

# sending a basic email
# connection = smtplib.SMTP(SMTP_URL)
# connection.starttls() #adding TLS security to the email.
# connection.login(user=USERNAME,password=PASSWORD)
# connection.sendmail(from_addr=EMAIL,to_addrs=RECIPIENT, msg="Subject:Message Here\n\nEmail Body.") #This now has a split up Subject field!
# connection.close()

# We can also do this with the 'with' keyword, just like we do with opening a file. That will auto-close the connection.
# with smtplib.SMTP(SMTP_URL) as connection:
#     connection.starttls() #adding TLS security to the email.
#     connection.login(user=USERNAME,password=PASSWORD)
#     connection.sendmail(from_addr=EMAIL,to_addrs=RECIPIENT, msg="Subject:Message Here\n\nEmail Body.")

# so a function would be:

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

def quote_grabber(text_path):
    """Grabs a random quote from a text file."""
    # I did it this way:
    # with open(text_path) as file:
    #     mylist=[]
    #     for line in file:
    #         mylist.append(line)
    #     return random.choice(mylist)
    # But I could've used list concatination to make this cleaner! This is all me:
    with open(text_path) as file:
        mylist = list(set([line for line in file]))
        return random.choice(mylist)
    # Using .readlines, which is what the course suggests, is nice too.
    # with open(text_path) as file:
    #     all_quotes = file.readlines()
    #     return random.choice(all_quotes)

# mock_email(SMTP_URL,USERNAME,PASSWORD,EMAIL,RECIPIENT,"Subject:Message Here\n\nEmail Body.")
# send_email(SMTP_URL,USERNAME,PASSWORD,EMAIL,RECIPIENT,"Subject:Message Here\n\nEmail Body.")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # This returns the day in 0-6 format (monday=0).
print(day_of_week)
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
if day_of_week == 4:
    mock_email(SMTP_URL,USERNAME,PASSWORD,EMAIL,RECIPIENT,"Subject:Here's your motivational quote!\n\n"+quote_grabber(QUOTES))