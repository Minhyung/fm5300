from fm_rest_api_binding import FmClient
import sys
import time
import getpass
from chassis_utils import ChassisUtils

#
# Sample script to reload card on a given node or cluster
#

if __name__ == '__main__':

    if len(sys.argv) != 6:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <CLUSTER ID> <CARD SLOT>\n")
        print("<CLUSTER ID> : Node IP or Cluster ID")
        print("<CARD SLOT>  : BoxId/SlotID (ex: 2/3 or 1/4)\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        clusterId = sys.argv[4]
        cardSlot = sys.argv[5]

    try:
        fm = FmClient(fmIp, fmUser, fmPasswd)

        c = ChassisUtils(fm)

        if c.reload_card(clusterId, cardSlot):
            print("ERROR: Card reload failed")
            sys.exit(1)
        else:
            print("Card reload successful")

    except Exception as e:
        print("Unable to access FM")
        raise e

    sys.exit(0)
