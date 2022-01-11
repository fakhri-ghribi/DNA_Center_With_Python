from dnacentersdk import api

DNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac.cisco.com")

DEVICES = DNAC.devices.get_device_list()

print("{0:15s}{1:1}{2:45s}{3:1}{4:17s}".format("DEVICE_Name", "|", "Model", "|", "UpTime"))

for DEVICE in DEVICES.response:
    print("{0:14s} {1:1} {2:15s} {3:1} {4:45s}".format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))

print("-"*90)


CLIENTS = DNAC.clients.get_overall_client_health("1686506489000")

print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format("Client Category", "|", "Number of Clients", "|", "Clients Score"))

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print("{0:25s}{1:1}{2:45s}{3:1}{4:<15d}".format(score.scoreCategory.value, "|", score.clientCount, "|",
                                                        score.scoreValue))

print("-"*90)

