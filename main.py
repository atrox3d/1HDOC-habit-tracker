import requests
import myob
import json


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
#
# create user: one shot
#
def create_user(username, token):
    user_params = {
        "username": username,
        "token": token,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    print(f"calling {PIXELA_ENDPOINT} with params: {user_params}")
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)
#
#   create graph: one shot
#
def create_graph(graph_id, name, unit, graph_type, color):
    graph_config = {
        "id":   graph_id,
        "name": name,
        "unit": unit,
        "type": graph_type,
        "color": color
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


create_user(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN)
create_graph("graph1", "Cycling Graph", "km", "float", "sora")
