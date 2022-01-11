import requests
from requests.auth import HTTPBasicAuth


def get_token():

    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    response = requests.post(url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify=False)
    print("token retreived {}".format(response.json()["Token"]))

if __name__ =="__main__":
    get_token()
