from twilio.rest import Client
from flight_data import FlightData


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self, configuration):
        self.config = configuration

    def send_sms(self, flight_data: FlightData):
        client = Client(self.config["TWILIO_SID"], self.config["TWILIO_AUTH"])
        message = client.messages.create(
            body=f"Low Price Alert! Only £{flight_data.price} to fly "
                 f"from {flight_data.from_city}-{flight_data.from_airport} "
                 f"to {flight_data.to_city}-{flight_data.to_airport}, "
                 f"from {flight_data.departure_date} to {flight_data.return_date}!",
            from_=self.config["TWILIO_NUMBER"], to=self.config["SMS_NUMBER"])
        print(message.status)
