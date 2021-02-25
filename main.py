import requests
import myob

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
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

