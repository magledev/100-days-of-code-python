import os
import requests

SHEETY_ENDPOINT = "<sheety_endpoint>"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
HEADERS = {"Authorization": f"Bearer {SHEETY_TOKEN}"}


class DataManager:
    # Communicates with Google Sheets api
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers=HEADERS)
        sheety_data = response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city}['id']", json=new_data
            )
            print(response.text)

    def add_new_user(self, first_name, last_name, email_address):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/users", headers=HEADERS)
        user_data = response.json()
        print(user_data)
        for user in user_data["users"]:
            if first_name == user["firstName"] and last_name == user["lastName"]:
                print(
                    "You are already signed up to Flight Club, please check your records or recover your details."
                )
            else:
                new_user_data = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "emailAddress": email_address,
                    }
                }
                response = requests.post(
                    url=f"{SHEETY_ENDPOINT}/users", headers=HEADERS, json=new_user_data
                )
                print(response.text, response.status_code)
