import requests
from flight_data import FlightData
import os
from pprint import pprint

TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    # Get city code from city query
    def get_destination_code(self, city_names):
        print("Get destination codes triggered")
        query_endpoint = f"{TEQUILA_API_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        for city in city_names:
            query_params = {"term": city_names, "location_types": "city"}
            query_response = requests.get(url=query_endpoint, headers=headers, params=query_params)
            query_results = query_response.json()["locations"]
            city_code = query_results[0]["code"]
            self.city_codes.append(city_code)
            return city_code

        # Search for flights using city code
    def search_flights(self, orig_city_code, dest_city_code, date_from, date_to):
        print(f"Check flights triggered for {dest_city_code}")
        search_endpoint = f"{TEQUILA_API_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        search_params = {
            "fly_from": orig_city_code,
            "fly_to": dest_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        search_response = requests.get(
            url=search_endpoint,
            headers=headers,
            params=search_params,
        )
        try:
            search_data = search_response.json()["data"][0]
        except IndexError:
            search_params["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_API_ENDPOINT}/v2/search",
                headers=headers,
                params=search_params,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=["route"][1]["cityTo"],
                to_airport=data["route"][1]["flyTo"],
                from_date=data["route"][0]["local_departure"].split("T")[0],
                to_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            pprint(data)
            return flight_data
        else:
            flight_data = FlightData(
                price=search_data["price"],
                from_airport=search_data["route"][0]["cityFrom"],
                to_airport=search_data["route"][0]["flyFrom"],
                to_city=search_data["route"][0]["cityTo"],
                from_city=search_data["route"][0]["flyTo"],
                from_date=search_data["route"][0]["local_departure"].split("T")[0],
                to_date=search_data["route"][1]["local_departure"].split("T")[0],
            )

        return flight_data
