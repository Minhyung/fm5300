from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
import sys
import os

#
# Script to add a device to FM
#

if __name__ == '__main__':

    if len(sys.argv) != 7:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <NODE IP> <NODE USER> <NODE PASSWORD>\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        nodeIp = sys.argv[4]
        nodeUser = sys.argv[5]
        nodePasswd = sys.argv[6]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    if ns.add_node_to_fm(nodeIp, nodeUser, nodePasswd):
        print("Add node to FM: FAIL")
    else:
        print("Add node to FM: PASS")

    sys.exit(0)
