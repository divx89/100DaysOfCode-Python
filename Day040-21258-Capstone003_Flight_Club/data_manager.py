import requests
from pprint import pprint


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self, config: dict):
        self.config = config

    def get_prices(self):
        return requests.get(url=self.config["SHEETY_URL"]+"/prices").json()["prices"]

    def get_users(self):
        return requests.get(url=self.config["SHEETY_URL"]+"/users").json()["users"]

    def put(self, row_id, row_data):
        put_url = f"{self.config['SHEETY_URL']}/prices/{row_id}"
        return requests.put(url=put_url, json=row_data)
