import requests
import myob
import json
#
# create user: one shot
#
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "username": myob.PIXELA_USERNAME,
    "token": myob.PIXELA_TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
print(f"calling {PIXELA_ENDPOINT} with params: {user_params}")
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
#
#   create graph: one shot
#
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}
#
# authentication via headers, not in the url
#
headers = {
    "X-USER-TOKEN": myob.PIXELA_TOKEN
}
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{myob.PIXELA_USERNAME}/graphs"
print(f"calling {GRAPH_ENDPOINT} with params: {graph_config} and headers: {headers}")
response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
print(f"get the graph here: {GRAPH_ENDPOINT}/{graph_config['id']}.html")

