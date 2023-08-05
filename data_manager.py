# This class is responsible for talking to the Google Sheet.
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/afd19828a0821d28e4e631967a1017e0/flightDeals2023/prices/"


class DataManager:
    def __init__(self, row_id):
        self.id = row_id

    def make_put_request(self, iata):
        sheet_parameters = {
            "price": {
                  "iataCode": iata,
            }
        }
        response = requests.put(url=SHEETY_ENDPOINT+str(self.id), json=sheet_parameters)
        response.raise_for_status()

