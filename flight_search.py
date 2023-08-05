import requests
from dotenv import  load_dotenv, dotenv_values
import os

load_dotenv()

API_KEY = os.getenv("FLIGHT_API_KEY")

header = {
    "apikey": API_KEY
}

location_endpoint = "https://api.tequila.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        city_name = ""

    def city_name(self, city):
        location_parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport"
        }

        response = requests.get(url=location_endpoint, params=location_parameters, headers=header)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code



