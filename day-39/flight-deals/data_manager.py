import requests

SHEETY_API_ENDPOINT = "<sheety_endpoint>"


class DataManager:
    # Communicates with Google Sheets api
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        sheety_data = response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)

    def update_prices(self):
        for city in self.destination_data:
            new_prices = {"price": {"lowestPrice": city["lowestPrice"]}}
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}", json=new_prices
            )
            print(response.text)
