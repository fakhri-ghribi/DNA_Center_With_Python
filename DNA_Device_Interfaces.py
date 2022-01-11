import json
import requests
from requests.auth import HTTPBasicAuth


def get_device_list():

    token = get_token()
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    query = {"x-auth-token": token, "Accept": "Application/json"}
    resp = requests.get(url, headers=query, verify=False)
    devices = resp.json()
    print(json.dumps(devices, indent=4))
    for device in devices["response"]:
        print(device["id"])

"""def print_device_list(devices):
    
    print("{0:10}{1:45}{3:25}{4:12}{5:20}{6:12}".format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for device in devices:
        print("{0:10}{1:45}{3:25}{4:12}{5:20}{6:12}".format(device["portName"], device["vlanId"], device["portMode"], device["portType"], device["duplex"], device["status"], device["lastUpdated"]))"""

def get_token():

    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    usr = "devnetuser"
    password = "Cisco123!"
    resp = requests.post(url, auth=HTTPBasicAuth(usr, password), verify=False)
    token = resp.json()["Token"]
    return token


get_device_list()
