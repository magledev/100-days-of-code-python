from datetime import datetime
import requests

USERNAME = "<username>"
TOKEN = "<token>"
DATE = datetime.now()
GRAPH = "sleep-tracker01"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
create_pixel_endpoint = f"{graph_endpoint}/{GRAPH}"
update_pixel_endpoint = f"{create_pixel_endpoint}/{DATE.strftime('%Y%m%d')}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH,
    "name": "Sarah's Step Tracker'",
    "unit": "Steps",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create a User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

# Create a Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Delete a Graph
# response = requests.delete(url=create_pixel_endpoint, headers=headers)
# print(response)

# Post a Pixel
# STEPS = input("How many steps did you take today?: ")
# pixel_config = {
#     "date": DATE.strftime("%Y%m%d"),
#     "quantity": STEPS,
#     # "optionalData": {"Notes": "Uphill, hot weather and humid. Tough ride."}
# }
# response = requests.post(url=create_pixel_endpoint, json=pixel_config, headers=headers)
# print(response)

# Update a Pixel
# response = requests.put(url=update_pixel_endpoint, json=pixel_config, headers=headers)
# print(response)

# Delete a Pixel
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response)
