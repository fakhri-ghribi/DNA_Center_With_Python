from dnacentersdk import api
DNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac.cisco.com")

DEVICES = DNAC.devices.get_device_list()

print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format("Device Name", "|", "Device Type", "|", "UP Time"))
print("-"*90)
for DEVICE in DEVICES.response:
    print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))

print("-"*90)


CLIENTS = DNAC.clients.get_overall_client_health(timestamp="1566506489000")

print("{0:25s}{1:1}{2:45s}{3:1}{4:15s}".format("Client Category", "|", "Number of Clients", "|", "Client Score"))
print("-" * 90)

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print("{0:25s}{1:1}{2:45s}{3:1}{4:<15d}".format(score.scoreCategory.value, "|", score.clientCount, "|", str(score.scoreValue)))