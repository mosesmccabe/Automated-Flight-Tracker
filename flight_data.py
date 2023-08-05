import requests
from datetime import datetime, timedelta
from pprint import pprint
import os
from dotenv import  load_dotenv, dotenv_values

load_dotenv()

flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"

API_KEY = os.getenv("FLIGHT_API_KEY")

header = {
    "apikey": API_KEY
}

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, iata_code):
        self.airport_ID = iata_code

    def search_for_flight(self):
        day = datetime.now()
        today = day.strftime("%d/%m/%Y")
        six_month_today = (day + timedelta(6*30)).strftime("%d/%m/%Y")
        cheap_flight = []

        parameter = {
            "fly_from": "SFO",
            "fly_to": self.airport_ID,
            "date_from": today,
            "date_to": six_month_today,
            "nights_in_dst_from": 10,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1,
            "vehicle_type": "aircraft",
            "ret_from_diff_airport": 0,
            "ret_to_diff_airport": 0,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "curr": "USD",
            "locale": "us",
            "limit": 1
        }

        response = requests.get(url=flight_search_endpoint, params=parameter, headers=header)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError: 
            return 0

        wanted_list_data = {"cityFrom": data["cityFrom"], "cityTo": data["cityTo"],
                     "from": data["route"][0]["local_departure"].split("T")[0],
                     "to": data["route"][-1]["local_departure"].split("T")[0],
                     "price": data["price"], "bookingLink": data["deep_link"]}
        return wanted_list_data
        # for item in data:
        #     dict_item = {"cityFrom": item["cityFrom"], "cityTo": item["cityTo"],
        #                  "localDeparture": item["local_departure"], "lengthOfStay": item["nightsInDest"],
        #                  "price": item["price"], "bookingLink": item["deep_link"]}
        #
        # return dict_item

    #         cheap_flight.append(list_item)
        #
        # return cheap_flight

