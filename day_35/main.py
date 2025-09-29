"""Grab openweathermap data: implement an API call providing a latitude and longitude, and add your API key.
Get your latitude and longitude from: https://www.latlong.net/
Get your API key from: https://openweathermap.org/api
If you want an example of a weather event, you can use https://www.ventusky.com/ and change the lat and long to that. (I did that.)
Also note this is needed: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/ If you're running this on pythonanywhere.
I didn't, so I didn't make this change."""
import requests
import datetime
from twilio.rest import Client

#Twilio Params. These are here because I'll never remember to edit them out in the function.
account_sid = ''
auth_token = ''
twilio_num = ''
my_num = ''

#API Params.
MY_LAT=""
MY_LON=""
API_KEY=""
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": MY_LAT,
    "lon": MY_LON, 
    "appid": API_KEY,
    "cnt": 4, # Number of results 
}

#Pull the openweather request for the last 12 hours.
openweather_request=requests.get(OWM_ENDPOINT,params)
openweather_request.raise_for_status()

def print_forecast():
    for forecast in openweather_request.json()['list']:
        # Convert epoch time to normal human time, and kalvin temp to fahrenheit, and print it for you.
        print("During", datetime.datetime.fromtimestamp(forecast['dt']).strftime('%c'), 
            "it will be", round(forecast['main']['temp'] * 1.8 - 459.67), "degrees F and ", forecast['weather'][0]['main'])

def check_for_rain():
    """Checks for if there will be any rain in the next 12 hours With a list comprehension and any!
    I'm gonna make myself get decent at this."""
    if any([forecast['weather'][0]['id'] < 700 for forecast in openweather_request.json()['list']]):
        return "It will rain, bring a jacket!"
    else:
        return "No rain, just go on ahead!!"

def send_whatsapp(text):
    """You need to prime the whatsapp connection before sending this on twilio's side. But this sends a whatsapp message.
    Uses a lot of the twilio variables defined at the top."""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=f'whatsapp:+{twilio_num}',
    body=text,
    to=f'whatsapp:+{my_num}'
    )


# print_forecast()
# print(check_for_rain())
send_whatsapp(check_for_rain())