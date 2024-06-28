import requests
from datetime import datetime
import os

# Nutrix API implementation
NUTRIX_ID = os.environ["NUTRIX_ID"]
NUTRIX_KEY = os.environ["NUTRIX_KEY"]

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout = input("Inform me of your workout. Type, duration etc: ").lower()
gender = input("Are you male or female?: ").lower()
weight = float(input("Please enter your bodyweight in Kg: "))
height = float(input("Please enter your height in cm: "))
age = int(input("How old are you?: "))

nutrix_parameters = {
    "query": workout,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

nutrix_headers = {
    "x-app-id": NUTRIX_ID,
    "x-app-key": NUTRIX_KEY,
    # "Content-Type": "json"
}

nutrix_response = requests.post(
    url=api_endpoint, json=nutrix_parameters, headers=nutrix_headers
)
data = nutrix_response.json()
print(nutrix_response)
print(data)

# Sheety API implementation
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_ENDPOINT = "<shhety_endpoint>"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    # "Content-Type": "application/json"
}

put_endpoint = f"{SHEETY_ENDPOINT}/2"

for item in data["exercises"]:
    sheety_parameters = {
        "record": {
            "date": str(datetime.date(datetime.now())),
            "time": str(datetime.time(datetime.now()).strftime("%H:%M:%S")),
            "exercise": item["name"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers
    )
    sheety_data = sheety_response.json()
    print(sheety_response)
    print(sheety_data)
