import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 50.414737
MY_LONG = -4.164006

OWM_API_KEY = os.environ.get("OWM_API_KEY")
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY,
    "units": "metric",
}

response = requests.get(OWM_API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_data = weather_data["hourly"][:12]

will_it_rain = False

for hour in hourly_data:
    if hour["weather"][0]["id"] <= 900:
        will_it_rain = True

if will_it_rain:
    proxy_client = TwilioHttpClient(
        proxy={"http": os.environ["http_proxy"], "https": os.environ["https_proxy"]}
    )
    client = Client(TWILIO_SID, TWILIO_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        from_="<tel_number>",
        to="<tel_number>",
        body="It's pretty much guaranteed to rain today. Bring a Brolly!!!",
    )
    print(message.status)
