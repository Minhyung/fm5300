from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
from port_utils import PortUtils
from map_utils import MapUtils
import sys
import os

#
# Script to update an existing map (with alias 'testMap')
#

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE STR>\n")
        print("\n<DEVICE STR>: Device IP or hostname\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        deviceStr = sys.argv[4]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    ms = MapUtils(fm, ns)

    payload = {
        'ruleId': 2,
        'comment': '',
        'bidi': False,
        'matches': [
             {     
                 'type': 'macSrc',
                 'value': '00:11:22:33:44:55'
             }   
        ]    
    }

    if ms.add_map_rule(deviceStr, "testMap", "pass", payload):
        print("Add map rule: FAIL")
    else:
        print("Add map rule: PASS")

    sys.exit(0)
