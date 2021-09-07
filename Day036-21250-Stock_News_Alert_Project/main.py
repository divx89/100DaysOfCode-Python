import requests
from dotenv import dotenv_values
from twilio.rest import Client

# Load the environment variables
config = dotenv_values(".env")

# Declare the constants for APIs
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_GO_URL = "https://www.alphavantage.co/query"
ALPHA_API_KEY = config["ALPHA_API_KEY"]

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config["NEWS_API_KEY"]

TWILIO_SID = config["TWILIO_SID"]
TWILIO_AUTH = config["TWILIO_AUTH"]

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increases/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_go_params = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": ALPHA_API_KEY}
alpha_response = requests.get(url=ALPHA_GO_URL, params=alpha_go_params)
alpha_response.raise_for_status()
last_two_days = [float(alpha_response.json()["Time Series (Daily)"][key]["4. close"])
                 for key in list(alpha_response.json()["Time Series (Daily)"].keys())[:2]]

percent_change = round(((last_two_days[0] - last_two_days[1]) / last_two_days[1]) * 100, 2)
symbol = "🔺" if percent_change >= 0 else "🔻"

if percent_change >= 5 or percent_change <= -5:

    print(f"Percentage Change in prices was {percent_change}. Getting news articles.")
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {"q": COMPANY_NAME, "pageSize": 3, "page": 1, "apiKey": NEWS_API_KEY}
    news_response = requests.get(url=NEWS_API_URL, params=news_parameters)
    news_response.raise_for_status()

    print("Got new articles. Sending an SMS for each")
    for article in news_response.json()["articles"]:
        title = article["title"]
        description = article["description"]
        # STEP 3: Use https://www.twilio.com
        # Send a separate message with the percentage change and each
        # article's title and description to your phone number.
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body=f"{STOCK}: {symbol}{percent_change}%\nHeadline: {title}\nBrief: {description}",
            from_=config["TWILIO_NUMBER"], to=config["SMS_NUMBER"])
        print(message.status)
else:
    print(f"Price change was {symbol}{percent_change}%. No action to be taken.")
