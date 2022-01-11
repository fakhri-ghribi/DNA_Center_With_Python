import json
import requests
URL = "https://webexapis.com/v1/memberships"
PAYLOAD = {
    "roomId": "jfdkjjkf",
    "name": "new_memeber300"
}
H = {
    "Authorization": "Bearer token",
    "Content-type": "application/json"
}
response = requests.post(URL, data=json.dumps(PAYLOAD) ,headers=H)
print(response.text)