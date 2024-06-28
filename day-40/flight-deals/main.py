from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManger

data_manager = DataManager()
flight_search = FlightSearch()
notification_manger = NotificationManger()

sheety_data = data_manager.get_destination_data()

ORIG_CITY_IATA = "LON"

print("To sign up to Flight Club you will need to provide your: First and Last name, along with your Email address.")
first_name = input("Please enter your First Name: ")
last_name = input("Please enter your Last Name: ")
email_address = input("Please enter a valid email address: ")
while email_address != input("Please confirm your Email address: "):
    print("The email address does not match. Please try again.")
data_manager.add_new_user(first_name=first_name, last_name=last_name, email_address=email_address)
print("Welcome to Flight Club. We hope you enjoy using our platform.")

if sheety_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheety_data]
    data_manager = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheety_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheety_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(weeks=26)

for destination_code in destinations:
    flight = flight_search.search_flights(
        ORIG_CITY_IATA,
        destination_code,
        date_from=tomorrow,
        date_to=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-{flight.origin_airport}" \
            f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. "
        if flight.stop_overs > 0:
            message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date} "

        notification_manger.send_emails(emails, message, link)
