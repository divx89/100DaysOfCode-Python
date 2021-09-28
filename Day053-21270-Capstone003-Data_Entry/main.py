import time
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from selenium import webdriver
import requests

config = dotenv_values(".env")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept-Language": "en-US,en;q=0.5"
}

zillow_sf_site = requests.get(url=config['ZILLOW_URL'], headers=headers).text
soup = BeautifulSoup(zillow_sf_site, "html.parser")

search_results = soup.select(selector=".list-card-info")
addresses = []
links = []
prices = []
for item in search_results:
    link = item.select_one(selector=".list-card-link")
    if link is not None:
        address = link.select_one(selector=".list-card-addr").text
        link = link.get("href") if link.get("href").startswith("http") else f"https://www.zillow.com{link.get('href')}"
        price = item.select_one(selector=".list-card-price").text
        price_string = price.split("/")[0].split(" ")[0].split("+")[0]
        links.append(link)
        prices.append(price_string)
        addresses.append(address)

print(addresses)
print(links)
print(prices)

driver = webdriver.Firefox(executable_path=config['GECKO_DRIVER'])

driver.get(url=config['FORMS_URL'])
time.sleep(2)

for n in range(len(addresses)):
    answer_areas = driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput")
    answer_areas[0].send_keys(addresses[n])
    answer_areas[1].send_keys(prices[n])
    answer_areas[2].send_keys(links[n])
    submit = driver.find_element_by_css_selector(".freebirdFormviewerViewNavigationSubmitButton")
    submit.click()
    time.sleep(2)
    next_response = driver.find_element_by_css_selector(".freebirdFormviewerViewResponseLinksContainer a")
    next_response.click()
    time.sleep(2)
