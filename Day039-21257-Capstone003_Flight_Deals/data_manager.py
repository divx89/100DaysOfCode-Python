import requests
from pprint import pprint


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self, config: dict):
        self.config = config

    def get(self):
        return requests.get(url=self.config["SHEETY_URL"]).json()["prices"]

    def put(self, row_id, row_data):
        put_url = f"{self.config['SHEETY_URL']}/{row_id}"
        return requests.put(url=put_url, json=row_data)
