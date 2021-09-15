# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import dotenv_values

# Load the environment variables
config = dotenv_values(".env")

# Initialize classes
data_manager = DataManager(config)
flight_search = FlightSearch(config)
notifier = NotificationManager(config)

# Get data from google sheets
sheet_data = data_manager.get()

for data in sheet_data:
    # For each row of data in the sheet, check if IATA Code is blank
    # If it is, get the correct code from API and update the
    if data['iataCode'] == '':
        iata_code = flight_search.get_iata_code(city_name=data['city'])
        data['iataCode'] = iata_code
        ret_data = data_manager.put(row_id=data['id'], row_data={'price': data})

    # Get flight data for each row of data
    flight_data = flight_search.get_flight_search(from_city="LON", price_ccy="GBP", sheet_data=data)

    # If the flight's price is less than the price in data, then send an sms
    if flight_data is not None and float(flight_data.price) <= data['lowestPrice']:
        print("Lower price detected! Send SMS!")
        notifier.send_sms(flight_data=flight_data)
    else:
        print(f"No flight found, or price in sheet (£{data['lowestPrice']}) is less than flight price")
