import requests
import myob
import json
from datetime import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def pixela_api(username, token, endpoint, params=None, moreheaders=None):
    """
    call pixela api, generalized
    """
    print(f"calling {endpoint}")
    if params:
        print(f"\twith params: {params}")
    # authentication via headers, not in the url
    headers = {"X-USER-TOKEN": token}
    # add more header keys, if available
    if moreheaders:
        headers.update(moreheaders)
    print(f"\twith headers: {headers}")
    #
    response = requests.post(url=endpoint, json=params, headers=headers)
    if response.status_code == 200:
        print("SUCCESS|status: ", response.status_code)
    else:
        print("ERROR  |status: ", response.status_code)
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
    response = pixela_api(username, token, PIXELA_ENDPOINT, user_params)
    # response.raise_for_status()
    return response


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
    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs"
    # print(f"calling {GRAPH_ENDPOINT}\nwith params: {graph_config}\nand headers: {headers}")
    # response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
    # print("response: ", response.text)
    response = pixela_api(username, token, GRAPH_ENDPOINT, graph_config)
    # response.raise_for_status()
    print(f"get the graph here: {GRAPH_ENDPOINT}/{graph_config['id']}.html")
    return response


def post_pixel(username, token, graphid, quantity, date=dt.now()):
    """
    post a single pixel in the specified graph
    """
    if isinstance(date, dt):
        date = str(date.date()).replace("-", "")
    if isinstance(date, str):
        # date = date.replace("-", "")
        pass

    params = {
        "date": date,
        "quantity": str(quantity)
    }
    PUTPIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{username}/graphs/{graphid}"
    response = pixela_api(username, token, PUTPIXEL_ENDPOINT, params)
    response.raise_for_status()
    return response


create_user(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN)
create_graph(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN, "graph1", "Cycling Graph", "km", "float", "sora")
post_pixel(myob.PIXELA_USERNAME, myob.PIXELA_TOKEN, "graph1", 1)
