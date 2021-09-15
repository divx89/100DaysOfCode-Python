from twilio.rest import Client
from flight_data import FlightData
import smtplib


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self, configuration):
        self.config = configuration

    def send_sms(self, flight_data: FlightData):
        client = Client(self.config["TWILIO_SID"], self.config["TWILIO_AUTH"])
        message_body = f"Low Price Alert! Only £{flight_data.price} to fly from " \
                       f"{flight_data.from_city}-{flight_data.from_airport} to " \
                       f"{flight_data.to_city}-{flight_data.to_airport}, from " \
                       f"{flight_data.departure_date} to {flight_data.return_date}!"
        if flight_data.stop_overs == 1:
            message_body += f"\nFlight has one stop-over, via {flight_data.via_city}"

        message = client.messages.create(
            body=message_body,
            from_=self.config["TWILIO_NUMBER"], to=self.config["SMS_NUMBER"])
        print(message.status)

    def send_emails(self, flight_data: FlightData, user_data):
        with smtplib.SMTP(self.config['SMTP_SERVER']) as connection:
            connection.starttls()
            connection.login(user=self.config['EMAIL_ID'], password=self.config['EMAIL_PASSWORD'])
            for user in user_data:
                message_body = f"Low Price Alert! Only £{flight_data.price} to fly from " \
                               f"{flight_data.from_city}-{flight_data.from_airport} to " \
                               f"{flight_data.to_city}-{flight_data.to_airport}, from " \
                               f"{flight_data.departure_date} to {flight_data.return_date}!"
                if flight_data.stop_overs == 1:
                    message_body += f"\nFlight has one stop-over, via {flight_data.via_city}"

                message_body += f"\nhttps://www.google.co.uk/flights?hl=en#flt={flight_data.from_airport}." \
                                f"{flight_data.to_airport}.{flight_data.departure_date}*{flight_data.to_airport}." \
                                f"{flight_data.from_airport}.{flight_data.return_date}"

                connection.sendmail(from_addr=self.config['EMAIL_ID'],
                                    to_addrs=user['email'],
                                    msg=f"Subject:New Low Price Flight!!\n\n{message_body}".encode("utf-8"))
