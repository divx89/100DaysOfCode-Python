from dotenv import dotenv_values
import datetime
import requests

# Load the environment variables
config = dotenv_values(".env")

USERNAME = config["USERNAME"]
TOKEN = config["TOKEN"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# [1] Create User in Pixela
pixela_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_user_params)
# print(response.text)

# [2] Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph01",
    "name": "Study Graph",
    "unit": "Hours",
    "type": "int",
    "color": "shibafu"
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(graph_response.text)

# [3] Create a new pixel
new_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"
new_pixel_params = {
    "date": f"{datetime.date.today().strftime('%Y%m%d')}",
    "quantity": "8"
}
# new_pixel_response = requests.post(url=new_pixel_endpoint, json=new_pixel_params, headers=graph_headers)
# print(new_pixel_response.text)

# [4] Modify a pixel
change_pixel_endpoint = f"{new_pixel_endpoint}/{datetime.date(year=2021, month=9, day=7).strftime('%Y%m%d')}"
change_pixel_params = {
    "quantity": "5"
}

# change_pixel_response = requests.put(url=change_pixel_endpoint, json=change_pixel_params, headers=graph_headers)
# print(change_pixel_response.text)

# [5] Delete a pixel
delete_pixel_endpoint = f"{new_pixel_endpoint}/{datetime.date(year=2021, month=9, day=7).strftime('%Y%m%d')}"
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=graph_headers)
# print(delete_pixel_response.text)
