import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 28.664420
MY_LON = 77.376670


def iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LON) <= 5:
        return True
    return False


def is_it_dark_out():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    if iss_overhead() and is_it_dark_out():
        print("ISS is overhead and it is dark out. Sending email.")
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="divx93416@yahoo.com", password="xtayuxsnvlblejos")
            connection.sendmail(from_addr="divx93416@yahoo.com",
                                to_addrs="divx93416@yahoo.com",
                                msg="Subject:The ISS is overhead!\n\nHey! Go outside! The ISS is overhead!")
    else:
        print("ISS is not overhead right now")
    print("Going to sleep now")
    time.sleep(60)
    print("Woke up. Next iteration, check for ISS and email")
