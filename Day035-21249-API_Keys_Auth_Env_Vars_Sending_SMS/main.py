import requests
from dotenv import dotenv_values
from twilio.rest import Client

# Load the environment variables
config = dotenv_values(".env")

# Declare the constants for API
API_KEY = config["OWM_API_KEY"]
ACCOUNT_SID = config["ACCOUNT_SID"]
AUTH_TOKEN = config["TWILIO_AUTH"]

# Declare the latitude and longitude
MY_LAT = 28.664419
MY_LON = 77.376671

# Parameters for the Open Weather Map API call
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

# Get the weather details
weather_response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather_response.raise_for_status()

# Find out if it will rain in the next 12 hours
it_will_rain = False
for hourly_data in weather_response.json()["hourly"][:12]:
    if hourly_data["weather"][0]["id"] < 700:
        it_will_rain = True
        break

print(it_will_rain)
# If it will rain in the next 12 hours, send an SMS
if it_will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="Hi! It's going to rain today, so carry an ☂️",
                                     from_=config["TWILIO_NUMBER"], to=config["SMS_NUMBER"])
    print(message.status)
