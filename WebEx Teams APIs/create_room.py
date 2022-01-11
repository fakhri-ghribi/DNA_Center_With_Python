import json
import requests

URL = "https://webexapis.com/v1/rooms"
Header = {
    "Authorization": "Bearer Cc8459310029556d20bd0ee78ef431b5be4e0e3e1da9d489c9d78d8748375fc69",
     "Content-type": "application/json"
}
PAYLOAD = {
    "name": "Devnet Room"
}
res = requests.post(URL, data=json.dumps(PAYLOAD), headers=Header)
print(res.text)