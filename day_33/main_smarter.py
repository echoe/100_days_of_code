"""Call up some APIs! This is """
import requests # my joy at not having to use urllib is boundless
import math
from datetime import datetime
import time
import smtplib # We don't use this, but just in case you really want to email someone ......
ISS_ENDPOINT="http://api.open-notify.org/iss-now.json"
SUNSET_ENDPOINT="https://api.sunrise-sunset.org/json"
MY_LAT=0.0
MY_LON=0.0
MY_EMAIL="email@example.com"
MY_PASSWORD="1234"
SMTP_URL="smtp.gmail.com" #Gmail's SMTP server.

def is_close_to_iss():
    """Return true if your location is currently close to the ISS, and false if it is not."""
    response = requests.get(url=ISS_ENDPOINT)
    if response.status_code != 200:
        response.raise_for_status()
    iss_location = response.json()['iss_position']
    iss_lat = iss_location['latitude']
    iss_lon = iss_location['longitude']
    if MY_LAT -5 <= iss_lat <= MY_LAT + 5 and MY_LON -5 <= iss_lon <= MY_LON + 5:
        return True
    else:
        return False

def is_sunset():
    """Returns true if we are in sunset, and false if we are not."""
    # {'results': {'sunrise': '11:42:31 AM', 'sunset': '11:40:24 PM', 'solar_noon': '5:41:27 PM', 'day_length': '11:57:53', 'civil_twilight_begin': '11:16:09 AM', 'civil_twilight_end': '12:06:46 AM', 'nautical_twilight_begin': '10:43:42 AM', 'nautical_twilight_end': '12:39:13 AM', 'astronomical_twilight_begin': '10:10:47 AM', 'astronomical_twilight_end': '1:12:08 AM'}, 'status': 'OK', 'tzid': 'UTC'}
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LON,
        "formatted":0,
    }
    sunresponse = requests.get(url=SUNSET_ENDPOINT, params=parameters)
    if sunresponse.status_code != 200:
        sunresponse.raise_for_status()
    sunrise = sunresponse.json()['results']['sunrise'].split("T")[1].split(':')[0]
    sunset = sunresponse.json()['results']['sunset'].split("T")[1].split(':')[0]
    time_now = datetime.now().hour
    if int(sunrise) > time_now > int(sunset):
        return True
    else:
        return False
    
def mock_email(my_msg):
    """Prints an email and all the things used to send an email. Does not send an email."""
    print(f"You sent an email to {MY_EMAIL} from {MY_EMAIL}! It said: Subject:Message Here\n\n{my_msg} \n"
          f"The email was sent with the credentials User: {MY_EMAIL} Password: {MY_PASSWORD} SMTP URL: {SMTP_URL}")

def send_email(my_msg):
    """Send an email with the required inputs, if you really wanna."""
    with smtplib.SMTP(SMTP_URL) as connection:
        connection.starttls() #adding TLS security to the email.
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg=my_msg)
while True:
    time.sleep(60)
    if is_sunset() and is_close_to_iss():
        mock_email("Look up!")
    else:
        print("Don't look up.")