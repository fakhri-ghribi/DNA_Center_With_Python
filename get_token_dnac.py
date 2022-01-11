import requests
from requests.auth import HTTPBasicAuth

#requests.packages.urllib3.disable_warning()

def get_auth_token():
    """

    """
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    response = requests.post(url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify = False)
    token = response.json()["Token"]
    print("Token Retrieved: {}".format(token))
    return token





if __name__ == "__main__":
  get_auth_token()

