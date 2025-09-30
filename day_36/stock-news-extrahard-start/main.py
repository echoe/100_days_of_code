import requests # We are gonna make some requests for sure.
from twilio.rest import Client # to send myself whatsapps.
STOCK = "INTL" # Put whatever stock you want here.
ALPHAVANTAGE_KEY=''
NEWSAPI_KEY=''

#Twilio Params. These are here because I'll never remember to edit them out down below.
account_sid = ''
auth_token = ''
twilio_num = ''
my_num = ''

#To send arrows;
up_arrow = '🔺'
down_arrow = '🔻'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock():
    """This compares just yesterday (the current day in the data) to the previous day.
    Returns whether change is pos or neg, change %, and GET_NEWS for the day in question.
    Only does this if the % change is larger than 5% day to day."""
    stock_url = f'https://www.alphavantage.co/query'
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': ALPHAVANTAGE_KEY,
    }
    stock_request = requests.get(stock_url, stock_params)
    stock_request_json = stock_request.json()
    # Now that we have the data, we process it. grab the current day and the previous close day values and do some math. here's also sample data if we want to test this working without putting API values in.
    # sample_data = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'INTL', '3. Last Refreshed': '2025-09-29', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2025-09-29': {'1. open': '27.8100', '2. high': '27.8200', '3. low': '27.6700', '4. close': '27.7583', '5. volume': '15073'}, '2025-09-26': {'1. open': '27.4900', '2. high': '27.6400', '3. low': '27.4600', '4. close': '27.6200', '5. volume': '32328'}}}
    current_day = next(iter(stock_request_json['Time Series (Daily)']))
    days = [f for f in list(stock_request_json['Time Series (Daily)'].values())[:2]]
    day_close = float(days[0]['4. close'])
    prevday_close = float(days[1]['4. close'])
    difference = int(100*(abs(prevday_close - day_close) / prevday_close))
    if difference > 5 and day_close>prevday_close:
        return [up_arrow, difference], get_news(current_day)
    elif difference > 5 and day_close < prevday_close:
        return [down_arrow, difference], get_news(current_day)
    else:
        return None
    # It was like this but I felt this was messy so I went back and fixed it. YMMV.
    # prevday_close = None
    # for day in list(time_series.items())[:2]: # Cut down to the last two items so we only check the last two days.
    #     day_close = float(day[1]['4. close'])
    #     if prevday_close != None:
    #         difference = abs(prevday_close - day_close)
    #         if (difference / prevday_close ) > 0.05: # If difference is larger than 5 percent, we make our message.
    #             if prevday_close > day_close:
    #                 updown = down_arrow
    #             else:
    #                 updown = up_arrow
    #             # print("hit on", day)
    #             news = get_news(day[0]) #Grab and return news articles for that day.
    #             return [updown, int(difference)], news

    #     prevday_close = day_close

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# There is an unofficial python package they recommend. Screw that though.
def get_news(day):
    """Put in a day, and this will use the NEWSAPI_KEY and the STOCK to get news data about the stock for the day.
    It returns the title, description, and then the URL of the first 3 pieces of news for the day in a list."""
    news_url = 'https://newsapi.org/v2/everything'
    news_params={
        'q':STOCK.lower(),
        'from':day,
        'to': day,
        'sortBy': 'popularity',
        'apiKey': NEWSAPI_KEY
    }
    news_request = requests.get(news_url, news_params)
    output = []
    for news in list(news_request.json()['articles'])[:3]:
        output.append({'title': news['title'], 'headline': news['description'], 'url': news['url']})
    return output

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_whatsapp(text):
    """You need to prime the whatsapp connection before sending this on twilio's side. But this sends a whatsapp message.
    Uses a lot of the twilio variables defined at the top."""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=f'whatsapp:+{twilio_num}',
    body=text,
    to=f'whatsapp:+{my_num}'
    )

info = get_stock()
if info != None:
    send_whatsapp(f"{STOCK}: {info[0][0]} {info[0][1]}%\nHeadline: {info[1][0]['title']}\nBrief:{info[1][0]['headline']}\nURL:{info[1][0]['url']}")