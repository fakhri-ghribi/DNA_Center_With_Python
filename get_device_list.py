import requests
from requests.auth import HTTPBasicAuth
#from dna_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD


def get_device_list():
    token = get_auth_token()
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    header = {"X-Auth-Token": token, "content-type": "application/json"}

    querystring = {"macAddres": "70:01:b5:5d:1b:00", "managementIpAddress": "10.10.20.80"}
    response = requests.get(url, headers=header, params=querystring, verify=False)

    device_list = response.json()
    print("ok")

    print_device_list(device_list)

def print_device_list(devices):

    print("{0:42}{1:17}{2:12}{3:18}{4:12}".format("Device Name", "|", "Device Type", "|", "Up Time"))
    print("-" * 95)
    for device in devices["response"]:
        print("{{0:42}{1:17}{2:12}{3:18}{4:12}".format(device["hostname"], "|", device["softwareType"], "|", device["upTime"]))


def get_auth_token():
    """
    """
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    response = requests.post(url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify = False)
    token = response.json()["Token"]
    return token



if __name__ == "__main__":
    get_device_list()
