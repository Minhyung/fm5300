from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
import sys
import os

#
# Script to remove a device from FM
#

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE STR>")
        print("\nDEVICE STR: Device IP or Device Hostname\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        deviceStr = sys.argv[4]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    if ns.delete_node(deviceStr):
        print("Delete node from FM: FAIL")
    else:
        print("Delete node from FM: PASS")

    sys.exit(0)
