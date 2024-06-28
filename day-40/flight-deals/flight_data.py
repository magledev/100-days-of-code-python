class FlightData:
    # Structures the flight data
    def __init__(self, price, from_city, to_city, from_airport, to_airport, from_date, to_date, stop_overs, via_city):
        self.price = price
        self.from_city = from_city
        self.to_city = to_city
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.from_date = from_date
        self.to_date = to_date
        self.stop_overs = stop_overs
        self.via_city = via_city
