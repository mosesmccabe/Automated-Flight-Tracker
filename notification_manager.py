import requests
import os
from dotenv import  load_dotenv, dotenv_values
from twilio.rest import Client
import smtplib

## TODO-1: setup email
my_email = "moses.peace.mccabe@gmail.com"
password = "imnxhuoeujhvlngw"

load_dotenv()

# Twilio api key and sid

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_API_KEY")
TWILIO_VIRTUAL_NUMBER = "18556418147"
TWILIO_VERIFIED_NUMBER = "15108388665"


class NotificationManager:
    def __init__(self, cheap_flight_list):
        self.info_list = cheap_flight_list

    def notification(self):

        # STEP 3: Use twilio.com/docs/sms/quickstart/python
        # Send a separate message with each article's title and description to your phone number.
        # HINT 1: Consider using a List Comprehension.
        body = f"Fly From: {self.info_list['cityFrom']} \nFly To: {self.info_list['cityTo']} \nPrice: ${self.info_list['price']}.00 \nFrom: {self.info_list['from']} \nTo: {self.info_list['to']} \nBooking Link: {self.info_list['bookingLink']} "
        # print(body)
        # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        # message = client.messages \
        #     .create(
        #     body=body,
        #     from_=TWILIO_VIRTUAL_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER
        # )
        # print(message.sid)

        # 4. Send the letter generated in step 3 to that person's email address.
        # HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # create a safe connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="moses.mccabe@outlook.com",
                                msg=f"Subject:Flight Deals\n\n{body}")