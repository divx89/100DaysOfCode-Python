from bs4 import BeautifulSoup
import requests
import json
from dotenv import dotenv_values
import smtplib

# Scraping an Amazon page for price info and sending email if price is below target

TARGET_PRICE = 130
PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept-Language": "en-US,en;q=0.5"
}

config = dotenv_values(".env")

page_response = requests.get(url=PRODUCT_URL, headers=headers)
page_response.raise_for_status()

soup = BeautifulSoup(page_response.text, "html.parser")
data_cart = soup.find_all(name="div", attrs={"class": "cardRoot"})[0].get("data-components")

data_dict = json.loads(data_cart)
price = float(f"{data_dict['1']['price']['wholeValue']}.{data_dict['1']['price']['fractionalValue']}")

if price < TARGET_PRICE:
    print("Price is lower than target. Send email")
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config['EMAIL_USER'], password=config['EMAIL_PASSWORD'])
        connection.sendmail(from_addr=config['EMAIL_USER'],
                            to_addrs=config['SEND_TO'],
                            msg=f"Subject:Instant Pot Pro 10-in-1 Pressure Cooker - Price Drop!\n\nInstant Pot Pro "
                                f"10-in-1 Pressure Cooker, Slow Cooker, Rice/Grain Cooker, Steamer, Sauté, Sous Vide, "
                                f"Yogurt Maker, Sterilizer, and Warmer, 6 Quart.\nNow available "
                                f"for only ${price}!\nVisit Now: {PRODUCT_URL}".encode('utf-8'))
