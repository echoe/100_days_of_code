"""Call up some APIs! This is """
import requests # my joy at not having to use urllib is boundless
import math
from datetime import datetime
import smtplib # We don't use this, but just in case you really want to email someone ......
ISS_ENDPOINT="http://api.open-notify.org/iss-now.json"
SUNSET_ENDPOINT="https://api.sunrise-sunset.org/json"
MY_LAT=0.0
MY_LONG=0.0
def call_iss():
    response = requests.get(url=ISS_ENDPOINT)
    if response.status_code != 200:
        response.raise_for_status()
    # iss_latitude = response.json()["iss_position"]['latitude']
    # iss_longitude = response.json()["iss_position"]['longitude']
    return(response.json()["iss_position"])

def call_sunset():
    """Returns if we are in sunset."""
    # {'results': {'sunrise': '11:42:31 AM', 'sunset': '11:40:24 PM', 'solar_noon': '5:41:27 PM', 'day_length': '11:57:53', 'civil_twilight_begin': '11:16:09 AM', 'civil_twilight_end': '12:06:46 AM', 'nautical_twilight_begin': '10:43:42 AM', 'nautical_twilight_end': '12:39:13 AM', 'astronomical_twilight_begin': '10:10:47 AM', 'astronomical_twilight_end': '1:12:08 AM'}, 'status': 'OK', 'tzid': 'UTC'}
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }
    sunresponse = requests.get(url=SUNSET_ENDPOINT, params=parameters)
    if sunresponse.status_code != 200:
        sunresponse.raise_for_status()
    sunrise = sunresponse.json()['results']['sunrise'].split("T")[1].split(':')[0]
    sunset = sunresponse.json()['results']['sunset'].split("T")[1].split(':')[0]
    time_now = datetime.now().hour
    if int(sunset) < time_now or int(sunrise) > time_now:
        return True
    else:
        return False
    
def mock_email(msg):
    """Prints an email and all the things used to send an email. Does not send an email."""
    smtp_url='smtp.com'
    to_addrs='myemail.com'
    from_addr='myemail.com'
    user='myemailuser'
    password='myemailpassword'
    print(f"You sent an email to {to_addrs} from {from_addr}! It said: Subject:Message Here\n\n{msg} \n"
          f"The email was sent with the credentials User: {user} Password: {password} SMTP URL: {smtp_url}")

iss_location = call_iss()
iss_lat_round = iss_location['latitude'].split('.')[0]
iss_lon_round = iss_location['latitude'].split('.')[0]
if int(iss_lat_round) + 5 >= int(str(MY_LAT).split('.')[0]) and int(iss_lat_round) - 5 <= int(str(MY_LAT).split('.')[0]): # If lat is within 5
    if int(iss_lon_round) + 5 >= int(str(MY_LONG).split('.')[0]) and int(iss_lon_round) - 5 <= int(str(MY_LONG).split('.')[0]): # If long is within 5
        if call_sunset() == True: # If we are in sunset
            print("Look up!")
        else:
            print("We are not in sunset but eventually you'll want to look up :)")
    else:
        print("We are not within longitude of the ISS.")
else:
    print("We are not within latitude of the ISS.")