from selenium import webdriver
from dotenv import dotenv_values
import time

SEARCH_URL = "https://www.linkedin.com/jobs/search/?geoId=109710172&keywords=python%20developer" \
             "&location=Bengaluru%2C%20Karnataka%2C%20India"
LOGIN_URL = "https://in.linkedin.com/"

GECKO_DRIVER = "C:/Users/divxd/Development/geckodriver.exe"

# [1] Load the environment variables
config = dotenv_values(".env")
USER_NAME = config["USER_NAME"]
PASSWORD = config["PASSWORD"]

driver = webdriver.Firefox(executable_path=GECKO_DRIVER)

driver.get(url=LOGIN_URL)

user_name_field = driver.find_element_by_id(id_="session_key")
password_field = driver.find_element_by_id(id_="session_password")
login_button = driver.find_element_by_css_selector(css_selector=".sign-in-form__submit-button")

user_name_field.send_keys(USER_NAME)
password_field.send_keys(PASSWORD)
login_button.click()

time.sleep(3)

driver.get(url=SEARCH_URL)
job_lists = driver.find_elements_by_css_selector(css_selector=".job-card-container")
for job in job_lists:
    job.click()
    time.sleep(3)
    job_save = driver.find_element_by_css_selector(css_selector=".jobs-save-button")
    job_save.click()

