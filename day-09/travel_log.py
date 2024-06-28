# Simple program to act as a travel log. Using  dictionaries and list.

travel_log = [
    {"country": "France",
     "total_visits": 12,
     "cities_visited": ["Paris", "Lille", "Dijon", "Bordeaux"],
     },
    {"country": "Germany",
     "total_visits": 7,
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart", "Dortmund"],
     },
]


def add_new_country(country_visited, times_visited, cities_visited):
    travel_log.append({"country": country_visited,
                      "total_visits": times_visited, "cities_visited": cities_visited})
    # new_country = {}
    # new_country["country"] = country_visited
    # new_country["total_visits"] = times_visited
    # new_country["cities_visited"] = cities_visited
    # travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "St Petersburg"])
print(travel_log)
