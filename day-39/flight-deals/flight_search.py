import requests
from flight_data import FlightData

TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "<tequila_api_key>"


class FlightSearch:
    # Get city code from city query
    def get_destination_code(self, city_name):
        query_endpoint = f"{TEQUILA_API_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query_params = {"term": city_name, "location_types": "city"}
        query_response = requests.get(
            url=query_endpoint, headers=headers, params=query_params
        )
        query_results = query_response.json()["locations"]
        city_code = query_results[0]["code"]
        return city_code

    def search_flights(self, orig_city_code, dest_city_code, date_from, date_to):
        # Search for flights using city code
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
            print(f"No flights available for {dest_city_code}")
            return None

        flight_data = FlightData(
            price=search_data["price"],
            from_airport=search_data["route"][0]["cityFrom"],
            to_airport=search_data["route"][0]["flyFrom"],
            to_city=search_data["route"][0]["cityTo"],
            from_city=search_data["route"][0]["flyTo"],
            from_date=search_data["route"][0]["local_departure"].split("T")[0],
            to_date=search_data["route"][0]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.to_city}: £{flight_data.price}")
        return flight_data
