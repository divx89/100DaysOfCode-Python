import requests
from dotenv import dotenv_values
import datetime

# Load the environment variables
config = dotenv_values(".env")
GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 175
AGE = 30

# Nutritionix API
NTX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = config["NTX_APP_ID"]
API_KEY = config["NTX_API_KEY"]

exercise_text = input("Enter the exercise you did: ")

ntx_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

ntx_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
ntx_response = requests.post(url=NTX_URL, json=ntx_body, headers=ntx_headers)
print(ntx_response.text)

SHEET_URL = config["SHEET_URL"]
sheet_headers={
    "Authorization": config["SHEET_AUTH_TYPE"]+" "+config["SHEET_AUTH_TOKEN"]
}

date_string = datetime.date.today().strftime("%d/%m/%Y")
time_string = datetime.datetime.now().strftime("%H:%M:%S")

for exercise in ntx_response.json()["exercises"]:
    body = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=SHEET_URL, json=body, headers=sheet_headers)
    print(sheet_response.text)
