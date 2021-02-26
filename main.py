import requests
import myob
import json

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def pixela_api(endpoint, params=None, headers=None):
    print(f"calling {endpoint}")
    if params:
        print(f"with params: {params}")
    if headers:
        print(f"with headers: {headers}")
    response = requests.post(url=endpoint, json=params, headers=headers)
    print("response: ", response.text)
    return response


def create_user(username: str, token: str):
    """
    create user: one shot
    """
    user_params = {
        "username": username,
        "token": token,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    # print(f"calling {PIXELA_ENDPOINT}\nwith params: {user_params}")
    # response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    # print("response: ", response.text)
    return pixela_api(PIXELA_ENDPOINT, user_params)


#
#   create graph: one shot
#
def create_graph(username, token, graph_id, name, unit, graph_type, color):
    """
    create graph: one shot
    """
    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": graph_type,
        "color": color
    }
    #
    # authentication via headers, not in the url
    #
    headers = {
        "X-USER-TOKEN": token
    }
    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs"
    # print(f"calling {GRAPH_ENDPOINT}\nwith params: {graph_config}\nand headers: {headers}")
    # response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
    # print("response: ", response.text)
    response = pixela_api(GRAPH_ENDPOINT, graph_config, headers)
    print(f"get the graph here: {GRAPH_ENDPOINT}/{graph_config['id']}.html")
    return response


create_user(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN)
create_graph(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN, "graph1", "Cycling Graph", "km", "float", "sora")
