import requests
import datetime
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, config: dict):
        """Initialize class with configuration data (e.g. tokens, URLs, etc)"""
        self.config = config

    def get_iata_code(self, city_name):
        """Get the IATA Code for a city"""
        query = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1
        }
        security = {"apikey": self.config["TEQUILA_API_KEY"]}
        url = f"{self.config['TEQUILA_URL']}/locations/query"
        return requests.get(url=url, params=query, headers=security).json()["locations"][0]["code"]

    def get_flight_search(self, from_city, price_ccy, sheet_data):
        """Get the data for a cheap flight out of 'from_city', to the data in 'sheet_data',
        with prices in 'price_ccy'"""
        query = {
            "fly_from": from_city,
            "fly_to": sheet_data["iataCode"],
            "date_from": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": price_ccy,
            "max_stopovers": 0
        }
        security = {"apikey": self.config["TEQUILA_API_KEY"]}
        url = f"{self.config['TEQUILA_URL']}/v2/search"
        response = requests.get(url=url, params=query, headers=security)

        # It is possible that there is no flight. In that case, return None
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No Non-stop flights found for {query['fly_to']}")
            print("Searching for 1 stop flights now")
            query['max_stopovers'] = 1
            response = requests.get(url=url, params=query, headers=security)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No 1-stop flights found for {query['fly_to']}")
                return None

        # Store the returned flight data as an object of a flight data class,
        # for easier access
        flight_data = FlightData(from_city=data["route"][0]["cityFrom"],
                                 to_city=data["route"][0]["cityTo"] if query['max_stopovers'] == 0 else
                                 data["route"][1]["cityTo"],
                                 from_airport=data["route"][0]["flyFrom"],
                                 to_airport=data["route"][0]["flyTo"] if query['max_stopovers'] == 0 else
                                 data["route"][1]["flyTo"],
                                 price=data["price"],
                                 departure_date=data["route"][0]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0])

        if query['max_stopovers'] == 1:
            flight_data.set_stopovers(stop_overs=1, via_city=data["route"][0]["cityTo"])

        print(f"{flight_data.to_city}: £{flight_data.price}")
        return flight_data
