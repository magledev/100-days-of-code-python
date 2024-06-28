from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManger
from flight_search import FlightSearch

data_manager = DataManager()
sheety_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manger = NotificationManger()

ORIG_CITY_IATA = "LON"

if sheety_data[0]["iataCode"] == "":
    for row in sheety_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheety_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheety_data:
    flight = flight_search.search_flights(
        ORIG_CITY_IATA,
        destination["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_today,
    )

    if flight.price < destination["lowestPrice"]:
        data_manager.update_prices()
