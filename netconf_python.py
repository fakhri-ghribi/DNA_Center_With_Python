from ncclient import manager

NXOS_HOST = "10.10.10.10"
NETCONF_PORT = "830"
USERNAME = "admin"
PASSWORD = "password"


def get_capabilities():

    with manager.connect(host=NXOS_HOST, port=NETCONF_PORT, username=USERNAME,password=PASSWORD,hostkey_verify=False) as device:
        print ("\n***NETCONG Capabilities for device {]***\n".format(NXOS_HOST))
        for cap in device.server_capabilities:
            print(cap)

if __name__=="__main__":
    get_capabilities()