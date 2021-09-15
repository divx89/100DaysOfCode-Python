import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, from_city, to_city, from_airport,
                 to_airport, price, departure_date, return_date):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.price = price
        self.departure_date = departure_date
        self.return_date = return_date
