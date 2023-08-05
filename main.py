# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from  data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager



sheety_endpoint = "https://api.sheety.co/afd19828a0821d28e4e631967a1017e0/flightDeals2023/prices"

sheet_parameters = {
    "price": {
        "city": "Liberia",
        "iataCode": "ROB",
        "lowestPrice": "1000"
    }
}

# push data onto sheety
# response = requests.post(url=sheety_endpoint, json=sheet_parameters)
# response.raise_for_status()
# pprint(response.text)

# get data from sheety
response = requests.get(url=sheety_endpoint)
response.raise_for_status()
sheet_data = response.json()["prices"]
# row_id = {data["id"] for data in sheet_data}

# data_manager = DataManager(row_id)
# data_manager.make_put_request()

# pprint(sheet_data)

flight_search = FlightSearch()
cheap_flight_list = []
for index, data in enumerate(sheet_data):
    if data["iataCode"] == "":
        # pass in city name and return airport IATA Code
        code_iata = flight_search.city_name(data["city"])
        # upload the IATA code to sheety
        data_manager = DataManager(data["id"])
        data_manager.make_put_request(code_iata)
    else:
        #airport_iata.append(data["iataCode"])
        # #Search for flight price
        flight_price = FlightData(data["iataCode"])
        cheap_flights_data = flight_price.search_for_flight()  # return a list of cheap flight info

        if not(cheap_flights_data == 0) and cheap_flights_data["cityTo"] == data["city"] and cheap_flights_data["price"] <= data["lowestPrice"]:
            print("data send")
            noti = NotificationManager(cheap_flights_data)
            noti.notification()

# ------------

#         if bool(cheap_flights_data):
#             print("processing")
#             dict_item = {"cityFrom": cheap_flights_data["cityFrom"], "cityTo": cheap_flights_data["cityTo"],
#                              "localDeparture": cheap_flights_data["local_departure"].split("T"), "from": cheap_flights_data["route"][0]["local_departure"].split("T")[0], "to": cheap_flights_data["route"][-1]["local_departure"].split("T")[0], "lengthOfStay": cheap_flights_data["nightsInDest"],
#                              "price": cheap_flights_data["price"], "bookingLink": cheap_flights_data["deep_link"]}
#
#             cheap_flight_list.append(dict_item)
#
#
# # if list is not empty: pass list (cheap_flight_list) to notification_manager.py to send a text message
# if cheap_flight_list:
#     print("not empty 2")
#     #noti = NotificationManager()
#     # compare cheap_flights with lowestPrice, I am willing to pay
#     for index, data in enumerate(cheap_flight_list):
#         # print(data)
#         if data["cityTo"] == sheet_data[index]["city"]:
#             if data["price"] <= sheet_data[index]["lowestPrice"]:
#                 noti = NotificationManager(data)
#                 noti.notification()


#
# else:
#     print("empty")


